
from .parser import replace_xml

class BackgroundWorker:

    @staticmethod
    def update_db():
        replace_xml("https://pypi.org/rss/packages.xml")
