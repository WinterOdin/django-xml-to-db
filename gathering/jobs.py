
from apscheduler.schedulers.background import BackgroundScheduler
from .background_worker import BackgroundWorker


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(BackgroundWorker.update_db, 'interval', seconds=1)
    scheduler.start()