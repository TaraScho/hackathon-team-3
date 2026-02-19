from typing import List, Dict, Any, Optional
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.api.events_api import EventsApi
from app.config import settings


class DatadogClient:
    """Wrapper for Datadog API client."""

    def __init__(self, api_key: Optional[str] = None, app_key: Optional[str] = None):
        self.api_key = api_key or settings.DATADOG_API_KEY
        self.app_key = app_key or settings.DATADOG_APP_KEY

        configuration = Configuration()
        configuration.api_key['apiKeyAuth'] = self.api_key
        configuration.api_key['appKeyAuth'] = self.app_key
        configuration.server_variables['site'] = settings.DATADOG_SITE

        self.api_client = ApiClient(configuration)
        self.hosts_api = HostsApi(self.api_client)
        self.metrics_api = MetricsApi(self.api_client)
        self.events_api = EventsApi(self.api_client)

    def get_infrastructure_list(self, filter_tags: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Fetch list of infrastructure hosts from Datadog."""
        try:
            response = self.hosts_api.list_hosts(filter=",".join(filter_tags) if filter_tags else None)

            hosts = []
            for host in response.host_list:
                hosts.append({
                    "name": host.name,
                    "tags": host.tags or [],
                    "meta": host.meta.to_dict() if host.meta else {},
                    "host_name": host.host_name,
                    "up": host.up
                })

            return hosts
        except Exception as e:
            raise Exception(f"Failed to fetch infrastructure list from Datadog: {e}")

    def get_host_by_name(self, host_name: str) -> Optional[Dict[str, Any]]:
        """Fetch specific host by name."""
        hosts = self.get_infrastructure_list()
        return next((h for h in hosts if h["name"] == host_name), None)

    def send_event(self, title: str, text: str, tags: Optional[List[str]] = None, alert_type: str = "info") -> str:
        """Send event to Datadog."""
        from datadog_api_client.v1.model.event_create_request import EventCreateRequest

        event = EventCreateRequest(
            title=title,
            text=text,
            tags=tags or [],
            alert_type=alert_type
        )

        response = self.events_api.create_event(body=event)
        return response.event.id

    def send_metric(self, metric_name: str, value: float, tags: Optional[List[str]] = None):
        """Send custom metric to Datadog."""
        from datadog_api_client.v1.model.metrics_payload import MetricsPayload
        from datadog_api_client.v1.model.series import Series
        import time

        series = Series(
            metric=metric_name,
            type="gauge",
            points=[[int(time.time()), value]],
            tags=tags or []
        )

        payload = MetricsPayload(series=[series])
        self.metrics_api.submit_metrics(body=payload)
