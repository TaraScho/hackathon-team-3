"""RQ worker process for executing drift detection jobs."""

import logging
from rq import Worker
from app.queue.tasks import redis_conn, queue

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start_worker():
    """Start the RQ worker to process jobs from the queue."""
    logger.info("Starting drift detection worker...")
    worker = Worker([queue], connection=redis_conn)
    worker.work()


if __name__ == "__main__":
    start_worker()
