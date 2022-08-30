
"""
* saját kivétel osztály létrehozása
* raise -zel kivétel objektum eldobása
"""

class NullavalValoOsztas(Exception):
    pass


def main():
    a = 5
    b = 0
    try:
        if b == 0:
            raise NullavalValoOsztas("nullaval nem lehet osztani")
        #
        result = a / b
        print(result)
    except NullavalValoOsztas as e:
        print(e)
    finally:
        print("END")

##############################################################################

if __name__ == "__main__":
    main()
