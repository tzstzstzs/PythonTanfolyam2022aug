
def f1():
    li = ['auto', 'villamos', 'metro']
    result = [s.upper() + "!" for s in li]
    print(result)

def f2():
    li = ['aladar', 'bela', 'cecil']
    result = [name.capitalize() for name in li]
    print(result)

def f3():
    result = [0 for i in range(10)]
    print(result)

def f4():
    li = [i for i in range(1, 10+1)]
    result = [n * 2 for n in li]
    print(result)

def f7():
    sentence = "The quick brown fox jumps over the lazy dog"
    result = [len(word) for word in sentence.split()]
    print(result)

def main():
    f1()
    print("-" * 40)
    f2()
    print("-" * 40)
    f3()
    print("-" * 40)
    f4()
    print("-" * 40)
    f7()

##############################################################################

if __name__ == "__main__":
    main()
