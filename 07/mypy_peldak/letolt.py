
import pyutils

def main():
    url = "https://www.python.org/"
    html = pyutils.get_page(url)
    print(html)

##############################################################################

if __name__ == "__main__":
    main()
