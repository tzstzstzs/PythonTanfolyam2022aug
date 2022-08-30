
import urllib.request

def get_page(url):
    response = urllib.request.urlopen(url)
    raw = response.read()
    # print(type(raw))
    html = raw.decode("utf-8")
    # print(type(html))
    # print(html)
    return html
