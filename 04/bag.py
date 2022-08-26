
class Bag:
    def __init__(self):
        self._data = []

    def add(self, value):
        self._data.append(value)
        # value mentése egy ab.-ba

    def add_twice(self, value):
        self.add(value)
        self.add(value)

    def __str__(self):
        return "Bag(" + str(self._data) + ")"

def main():
    b = Bag()
    b.add(5)
    b.add(7)
    print(b)
    b.add_twice(9)
    print(b)

##############################################################################

if __name__ == "__main__":
    main()
