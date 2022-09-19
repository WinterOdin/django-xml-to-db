import re
import json
import requests
import pandas as pd
from .models import Package
from requests_html import HTML
from sqlalchemy import create_engine
from django.http import HttpResponse
from requests_html import HTMLSession
from rest_framework.response import Response


def get_source(url: str) -> Response:
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


def get_details(package_name: str) -> dict:
    """Returns a python dictionary containing detaild 
        data about the package.

    Args: 
        package_name (string): URL of the RSS feed to read.

    Returns:
        dict (dictionary): containing the detail information.
    """

    response = get_source(f'https://pypi.org/pypi/{package_name.lower().strip()}/json')
    if response.status_code == 200:

        data = json.loads(response.text)
        context = {
            'name': data['info']['author'] or 'No name found',
            'version': data['info']['version'] or 'No version found',
            'keywords': data['info']['keywords'] or 'No keywords found',
        }
    else:

        context = {
            'name': 'No detail found',
            'version': 'No detail found',
            'keywords': 'No detail found',
        }

    return context


def get_feed(url: str) -> pd.DataFrame:
    """Return a Pandas dataframe containing the RSS feed contents.

    Args: 
        url (string): URL of the RSS feed to read.

    Returns:
        df (dataframe): Pandas dataframe containing the RSS feed contents.
    """

    response = get_source(url)
    df = pd.DataFrame(columns=['title', 'link', 'description', 'author', 'email', 'keywords', 'version' 'pubDate'])
    tmp = []
    with response as r:
        items = r.html.find("item", first=False)

        for item in items:
            title = re.split('added to PyPI', item.find('title', first=True).text)[0]
            link = item.find('guid', first=True).text
            pubDate = item.find('pubDate', first=True).text
            description = item.find('description', first=True).text or 'No description'
            data = get_details(title)
            author = data['name']
            version = data['version']
            keywords = data['keywords']
            try:
                #
                email = item.find('author', first=True).text
            except AttributeError:
                email = 'No email'

            row = {'title': title, 'link': link, 'description': description, 'author': author, 'email': email,
                   'keywords': keywords, 'version': version, 'pubDate': pubDate}
            tmp.append(row)

        df = pd.DataFrame(tmp)

    return df


def save_xml(url: str) -> None:
    """Saves a Pandas dataframe to db.

    Args: 
        url (string): URL of the RSS feed to read.
    """

    df = get_feed(url)
    engine = create_engine('sqlite:///db.sqlite3')
    df.to_sql(Package._meta.db_table, if_exists='replace', con=engine, index=True, index_label='id')
