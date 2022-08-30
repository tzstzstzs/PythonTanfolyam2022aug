
def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ZeroDivisionError:
            print("Hiba: 0-val nem lehet osztani!")
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Hiba: számot adj meg!")

#####

if __name__ == "__main__":
    main()
