"""
sorted():
---------
* kap egy listát
* listáról készít egy másolatot
* a másolatot rendezi
* visszaadja a rendezett másolatot
"""

import random

def shuffled(li):
    copy = li.copy()
    random.shuffle(copy)
    return copy

def main():
    li = [1, 2, 3, 4, 5]
    kevert = shuffled(li)
    print(li)  # [1, 2, 3, 4, 5]
    print(kevert)    # pl. [5, 1, 3, 2, 4]

##############################################################################

if __name__ == "__main__":
    main()
