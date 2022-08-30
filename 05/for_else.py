
def main():
    for i in range(10):
        print(i, end=' ')
        if i == 15:
            break
    else:    # nobreak
        print()
        print("there was no break")


##############################################################################

if __name__ == "__main__":
    main()
