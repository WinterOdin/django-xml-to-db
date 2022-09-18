from .parser import save_xml


class BackgroundWorker:

    @staticmethod
    def update_db():
        save_xml("https://pypi.org/rss/packages.xml")
