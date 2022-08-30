
import requests

def main():
    url = "https://www.python.org/"
    r = requests.get(url)
    html = r.text
    print(type(html))

##############################################################################

if __name__ == "__main__":
    main()
