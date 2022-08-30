
def valami(name, _id, age=20):
    print(f"Name: {name}, ID: {_id}, age: {age}")


def main():
    valami("Laci", "XZ25", age=35)
    # valami("Laci", "XZ25", 35)
    # valami(name="Laci", _id="XZ25", age=35)
    # valami(_id="XZ25", name="Laci", age=35)
    # valami(name="Laci", "XZ25", 35) # Hiba! keyword argument után nem jöhet positional argument
    # valami("Laci", _id="XZ25", 35) # Hiba! Ugyanezen ok ^^^ miatt.

##############################################################################

if __name__ == "__main__":
    main()
