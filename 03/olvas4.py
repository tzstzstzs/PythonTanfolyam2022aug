
def main():
    f = open("szoveg.txt", "r")

    elso = f.readline()
    masodik = f.readline()

    print("'" + elso + "'")
    print("'" + masodik + "'")

    f.close()

##############################################################################

if __name__ == "__main__":
    main()
