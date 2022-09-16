import requests
import pandas as pd
from .models import Package
from requests_html import HTML
from sqlalchemy import create_engine
from django.http import HttpResponse
from requests_html import HTMLSession
import re

def get_source(url: str) -> HttpResponse:
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def get_feed(url: str) -> pd.DataFrame:
    """Return a Pandas dataframe containing the RSS feed contents.

    Args: 
        url (string): URL of the RSS feed to read.

    Returns:
        df (dataframe): Pandas dataframe containing the RSS feed contents.
    """
    
    response = get_source(url)
    df = pd.DataFrame(columns = ['title', 'link', 'description', 'author', 'pubDate'])
    tmp = []
    with response as r:
        items = r.html.find("item", first=False)
        
        for item in items:
            title = re.split('added to PyPI', item.find('title', first=True).text)[0]
            link = item.find('guid', first=True).text
            pubDate = item.find('pubDate', first=True).text
            description = item.find('description', first=True).text or 'No description'

            try:
                author = item.find('author', first=True).text
            except AttributeError:
                author = 'No author'
            
            row = {'title': title, 'link': link, 'description': description, 'author': author, 'pubDate': pubDate}
            tmp.append(row)
           

        df = pd.DataFrame(tmp)

    return df

def replace_xml(url: str):
    """Saves a Pandas dataframe to db.

    Args: 
        url (string): URL of the RSS feed to read.
    """

    df = get_feed(url)
    engine = create_engine('sqlite:///db.sqlite3')
    df.to_sql(Package._meta.db_table, if_exists='replace', con=engine, index=True, index_label='id')

