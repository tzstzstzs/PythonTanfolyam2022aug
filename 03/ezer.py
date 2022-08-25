
N = 1_000

def main():
    szamok = [n for n in range(1, N) if n % 3 == 0 or n % 5 == 0]
    print(sum(szamok))

##############################################################################

if __name__ == "__main__":
    main()
