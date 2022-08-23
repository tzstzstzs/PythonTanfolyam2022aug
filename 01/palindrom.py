
def is_palindrome(s):
    return s == s[::-1]


def main():
    s = "apa"
    print(f"{s} palindrom?", is_palindrome(s))

##############################################################################

if __name__ == "__main__":
    main()
