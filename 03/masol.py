
INPUT = "szoveg.txt"
OUTPUT = "masolat.txt"

def main():
    f1 = open(INPUT, "r")
    to = open(OUTPUT, "w")

    for line in f1:
        to.write(line)

    f1.close()
    to.close()

    print("END")

##############################################################################

if __name__ == "__main__":
    main()
