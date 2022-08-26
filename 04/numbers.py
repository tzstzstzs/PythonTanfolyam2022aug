
INPUT = "numbers.txt"

def main():
    total = 0
    with open(INPUT) as f:
        for line in f:
            total += int(line)
        #
    #
    print(total)
    result = str(total)[:10]
    print(result)

##############################################################################

if __name__ == "__main__":
    main()
