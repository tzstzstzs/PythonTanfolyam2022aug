
def main():
    f = open("szoveg.txt", "r")

    lines = f.readlines()
    print(lines)

    f.close()

##############################################################################

if __name__ == "__main__":
    main()
