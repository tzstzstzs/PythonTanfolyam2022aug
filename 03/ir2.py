
def main():
    f = open("out2.txt", "w")

    print("hello", file=f)
    f.write("py\n")
    f.write("thon\n")

    f.close()

    print("END")

##############################################################################

if __name__ == "__main__":
    main()
