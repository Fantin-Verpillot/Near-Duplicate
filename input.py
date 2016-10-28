import urllib.request
import re
from bs4 import BeautifulSoup


def get_content(url):
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        texts = soup.findAll(text=True)

        def visible(element):
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
                return False
            elif re.match('<!--.*-->', str(element)):
                return False
            return True

        visible_texts = ''.join(list(filter(visible, texts)))
        return visible_texts, 200

    except urllib.error.HTTPError as HttpErr:
        return 'HTTP Error: ' + str(HttpErr.code) + ' -> ' + url, 400
    except urllib.error.URLError as UrlErr:
        return str(UrlErr.reason) + ' -> ' + url, 500
    except ValueError:
        return 'Error: Value incorrect -> ' + url, 501
