

def my_func1(t):
    return t[-1]


def f1():
    data = [
        (1, 'Albany', 'NY', 162692),
        (3, 'Allegany', 'NY', 11986),
        (121, 'Wyoming', 'NY', 8722),
        (123, 'Yates', 'NY', 5094)
    ]
    # result = sorted(data, key=my_func1)
    result = sorted(data, key=lambda t: t[-1])
    print(result)


def my_func2(user):
    return int(user.split(":")[0])

def f2():
    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

    result = sorted(users, key=my_func2, reverse=True)
    print(result)


def my_func3(sor):
    return sor[1]


def f3():
    matrix = [ [2, 6], [1, 3], [5, 4] ]
    # result = sorted(matrix, key=my_func3)
    result = sorted(matrix, key=lambda sor: sor[1])
    print(result)

def main():
    # f1()
    # f2()
    f3()

##############################################################################

if __name__ == "__main__":
    main()
