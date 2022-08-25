
def main():
    f = open("szoveg.txt", "r")

    for line in f:
        line = line.rstrip("\n")
        if line.endswith("line."):
            print(line)

    f.close()

##############################################################################

if __name__ == "__main__":
    main()
