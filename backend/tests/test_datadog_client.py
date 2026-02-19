import pytest
from unittest.mock import Mock, patch
from app.services.datadog_client import DatadogClient


@pytest.fixture
def datadog_client():
    return DatadogClient(api_key="test_key", app_key="test_app_key")


def test_get_infrastructure_list(datadog_client):
    """Test fetching infrastructure list from Datadog."""
    with patch('datadog_api_client.v1.api.hosts_api.HostsApi.list_hosts') as mock_list:
        mock_response = Mock()
        mock_host1 = Mock()
        mock_host1.name = "web-server-1"
        mock_host1.tags = ["env:production", "team:backend"]
        mock_host1.meta = None
        mock_host1.host_name = "web-server-1"
        mock_host1.up = True

        mock_host2 = Mock()
        mock_host2.name = "web-server-2"
        mock_host2.tags = ["env:production", "team:backend"]
        mock_host2.meta = None
        mock_host2.host_name = "web-server-2"
        mock_host2.up = True

        mock_response.host_list = [mock_host1, mock_host2]
        mock_list.return_value = mock_response

        hosts = datadog_client.get_infrastructure_list()

        assert len(hosts) == 2
        assert hosts[0]["name"] == "web-server-1"
        assert "env:production" in hosts[0]["tags"]


def test_get_host_by_name(datadog_client):
    """Test fetching specific host by name."""
    with patch('datadog_api_client.v1.api.hosts_api.HostsApi.list_hosts') as mock_list:
        mock_response = Mock()
        mock_host = Mock()
        mock_host.name = "web-server-1"
        mock_host.tags = ["env:production"]
        mock_host.host_name = "web-server-1"
        mock_host.up = True
        mock_meta = Mock()
        mock_meta.agent_version = "7.0.0"
        mock_host.meta = mock_meta

        mock_response.host_list = [mock_host]
        mock_list.return_value = mock_response

        host = datadog_client.get_host_by_name("web-server-1")

        assert host is not None
        assert host["name"] == "web-server-1"
