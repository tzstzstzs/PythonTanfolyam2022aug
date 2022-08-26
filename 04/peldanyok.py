
class Example:
    counter = 0

    def __init__(self):
        Example.counter += 1

def main():
    e1 = Example()
    e2 = Example()
    print(Example.counter)   # 2
    e3 = Example()
    print(Example.counter)   # 3

##############################################################################

if __name__ == "__main__":
    main()
