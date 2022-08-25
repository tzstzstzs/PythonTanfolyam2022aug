
def main():
    f = open("out.txt", "w")

    print("hello", file=f)
    print("world", file=f)
    print(2022, file=f)

    f.close()

    print("END")

##############################################################################

if __name__ == "__main__":
    main()
