from django.apps import AppConfig


class GatheringConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gathering'

    def ready(self):
        import os
        from . import jobs

        if os.environ.get('RUN_MAIN', None) != 'true':
            jobs.start()
