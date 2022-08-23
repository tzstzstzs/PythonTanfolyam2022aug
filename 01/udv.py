
"""
    udv.py Batman
    Denevérveszély!
    
    udv.py Laci
    Hello Laci!
    
    else if -> elif
"""

import sys


def hello(nev):
    if (nev == "Batman") or (nev == "Robin"):
        print("Denevérveszély!")
    else:
        print("Hello " + nev + "!")


def main():
    name = sys.argv[1]
    hello(name)
    
    
if __name__ == "__main__":
    main()