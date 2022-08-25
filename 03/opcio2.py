
def hello(name, repeat=1, postfix=""):
    for _ in range(repeat):
        print(name + postfix)


def main():
    # hello("Laci")
    # print("-" * 10)
    # hello("Anna", repeat=2)
    # print("-" * 10)
    # hello("Bela", repeat=3, postfix="!")
    # print("-" * 10)
    hello("Bela", repeat=3, postfix="!")

##############################################################################

if __name__ == "__main__":
    main()
