"""
írassuk ki a 100-nál kisebb prímszámokat (ex1.py)
"""

import pygyak

def main():
    result = [n for n in range(2, 100) if pygyak.is_prime(n)]
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
