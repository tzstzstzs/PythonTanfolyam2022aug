
import requests

def main():
    url = "https://jsonip.com/"
    r = requests.get(url)

    d = r.json()

    ip = d['ip']

    print(f"Az On IP cime: {ip}")

##############################################################################

if __name__ == "__main__":
    main()
