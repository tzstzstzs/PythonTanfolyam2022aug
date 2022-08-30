
class Verem:
    def __init__(self):
        self._data = []

    def betesz(self, value):
        self._data.append(value)

    def ures(self):
        return len(self._data) == 0

    def meret(self):
        return len(self._data)

    def kivesz(self):
        if self.ures():
            return None
        # else
        return self._data.pop()

    def __str__(self):
        return str(self._data)[:-1]

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

##############################################################################

if __name__ == "__main__":
    main()
