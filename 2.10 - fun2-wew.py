# funkcja wewnetrzna (zagnieżdzona)
# funkcje wewnetrzne są wykorzystane przy dekoratorach

def fun1():
    print("To jest funkcja fun1")

    def fwew(a, b):
        return a * b

    return fwew  # zwracamy adres funkcji (referencje)


x = fun1()  # To jest funkcja fun1
print(x)  # <function fun1.<locals>.fwew at 0x000001E213EC9F80>
print(type(x))  # <class 'function'>
print(x(8, 9))  # 72
