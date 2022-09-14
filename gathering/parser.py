import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

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

def get_feed(url: str) -> pd.DataFrame:
    """Return a Pandas dataframe containing the RSS feed contents.

    Args: 
        url (string): URL of the RSS feed to read.

    Returns:
        df (dataframe): Pandas dataframe containing the RSS feed contents.
    """
    
    response = get_source(url)
    
    df = pd.DataFrame(columns = ['title', 'link', 'description', 'author', 'pubDate'])

    with response as r:
        items = r.html.find("item", first=False)

        for item in items:        

            title = item.find('title', first=True).text
            link = item.find('link', first=True).text
            pubDate = item.find('pubDate', first=True).text
            description = item.find('description', first=True).text
            author = item.find('author', first=True).text

            row = {'title': title, 'link': link, 'description': description, 'author': author, 'pubDate': pubDate}
            df = df.append(row, ignore_index=True)

    return df