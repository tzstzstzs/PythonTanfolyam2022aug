
import json
import requests

def main():
    url = "https://jsonip.com/"
    r = requests.get(url)
    s = r.text
    # print(s)
    d = json.loads(s)
    # print(d)
    ip = d['ip']
    # print(ip)
    print(f"Az On IP cime: {ip}")

##############################################################################

if __name__ == "__main__":
    main()
