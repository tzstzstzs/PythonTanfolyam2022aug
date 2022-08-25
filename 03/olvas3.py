
def main():
    f = open("szoveg.txt", "r")

    tartalom = f.read()
    print("'" + tartalom + "'")
    print("---")
    sorok = tartalom.splitlines()
    print(sorok)

    f.close()

##############################################################################

if __name__ == "__main__":
    main()
