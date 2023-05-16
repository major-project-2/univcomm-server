from app.core.config import settings
from celery import Celery

celery_app = Celery(__name__, broker=settings.CELERY_BROKER_URL,
                    backend=settings.CELERY_RESULT_BACKEND)

celery_app.conf.update(
    timezone='Asia/Calcutta',
    enable_utc=False
)
