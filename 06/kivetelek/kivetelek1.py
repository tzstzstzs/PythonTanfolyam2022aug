
def main():
    a = 5
    b = 0

    try:
        result = a / b
        print(f"{result=}")
    except:
        print("Hopp! Kivetel!")
    else:
        print("minden oke")
    finally:
        print("END")

##############################################################################

if __name__ == "__main__":
    main()
