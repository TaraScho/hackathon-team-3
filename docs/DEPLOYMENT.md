# DriftGuard Deployment Guide

## Prerequisites

- Docker and Docker Compose
- Datadog API credentials
- Git repositories to monitor

## Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/TaraScho/hackathon-team-3.git
   cd hackathon-team-3
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your Datadog credentials
   ```

3. **Start services**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Production Deployment

### Kubernetes Deployment

1. **Create secrets**
   ```bash
   kubectl create secret generic driftguard-secrets \
     --from-literal=database-url=<your-db-url> \
     --from-literal=datadog-api-key=<your-api-key> \
     --from-literal=datadog-app-key=<your-app-key>
   ```

2. **Apply manifests**
   ```bash
   kubectl apply -f k8s/
   ```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| DATABASE_URL | PostgreSQL connection string | Yes |
| REDIS_URL | Redis connection string | Yes |
| DATADOG_API_KEY | Datadog API key | Yes |
| DATADOG_APP_KEY | Datadog application key | Yes |
| DATADOG_SITE | Datadog site (default: datadoghq.com) | No |
| SECRET_KEY | Application secret key | Yes |
| APP_ENV | Environment (development/production) | No |
| LOG_LEVEL | Logging level | No |

## Monitoring

DriftGuard automatically sends metrics and events to Datadog:

- **Metrics**: `driftguard.drift.count`, `driftguard.detection.duration_ms`
- **Events**: Drift detection alerts
- **Logs**: Structured application logs

## Troubleshooting

### Worker not processing jobs

Check worker logs:
```bash
docker-compose logs worker
```

Verify Redis connection:
```bash
docker-compose exec redis redis-cli ping
```

### Database migration issues

Run migrations manually:
```bash
docker-compose exec backend alembic upgrade head
```
