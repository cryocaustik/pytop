from django.conf import settings
import psutil
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from api.models import Proc


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
CPU_COUNT = psutil.cpu_count()


@register_job(
    scheduler,
    "interval",
    seconds=settings.APSCHEDULER_INTERVAL_SECONDS,
    replace_existing=True,
)
def get_all_procs():
    for p in psutil.process_iter():
        proc = Proc(
            pid=p.pid,
            name=p.name(),
            mem=p.memory_percent(),
            cpu=p.cpu_percent() / CPU_COUNT,
        )
        proc.save()


register_events(scheduler)
if settings.APSCHEDULER_AUTOSTART:
    scheduler.start()
