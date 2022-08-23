
import sys

def main():
    if len(sys.argv) != 3:
        print("Hiba! Pontosan ket argumentum kell!", file=sys.stderr)
        sys.exit(1)
    # else
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    print(n1 + n2)

##############################################################################

if __name__ == "__main__":
    main()
