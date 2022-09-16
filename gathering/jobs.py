
from apscheduler.schedulers.background import BackgroundScheduler
from .background_worker import BackgroundWorker
from datetime import datetime, timedelta

def start():    
    scheduler = BackgroundScheduler(timezone='EU/Warsaw')
    scheduler.add_job(BackgroundWorker.update_db, 'interval', hours=24, next_run_time=datetime.now() + timedelta(0,10))
    scheduler.start()