"""
írassuk ki a 200-nál kisebb prímszámok összegét (ex2.py)
"""

import pygyak

def main():
    result = sum([n for n in range(2, 200) if pygyak.is_prime(n)])
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
