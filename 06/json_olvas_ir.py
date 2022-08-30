
import json
from pprint import pprint

def main():
    fname = "person.json"
    with open(fname, "r") as f:
        d = json.load(f)
    #

    d["wife"]["age"] = 30

    to = open("younger.json", "w")
    json.dump(d, to, indent=2)
    to.close()

##############################################################################

if __name__ == "__main__":
    main()
