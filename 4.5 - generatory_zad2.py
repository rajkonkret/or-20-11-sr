generator_1 = [x for x in range(5)]
print(type(generator_1))  # <class 'list'>
generator_2 = (x for x in [1, 2, 3, 4, 5])  # jednolinijkowo stworzony generator
print(type(generator_2))  # <class 'generator'>
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


def generator_3():
    for x in [1, 2, 3, 4, 5]:
        yield x


def gen_4():
    yield [x for x in [1, 2, 3]]


g4 = gen_4()
print(next(g4))  # [1, 2, 3]


def gen_5():
    i = 1
    while True:
        yield i * i
        i += 1


g5 = gen_5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fi = fibo()
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fi2 = fibo_with_index(10)
print(next(fi2))  # (0, 0)
for i in fibo_with_index(5):
    print(f"elemnt {i}")

for i, n in fibo_with_index(5):
    print(f"pozycja {i}: elemnt {n}")


# pozycja 0: elemnt 0
# pozycja 1: elemnt 1
# pozycja 2: elemnt 1
# pozycja 3: elemnt 2
# pozycja 4: elemnt 3

def counter(start=0):
    n = start
    while True:
        result = yield n
        print(result)  # wyswietlenie przekazanego komunikatu
        if result == 'q':
            break
        n += 1


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(c.send('OK'))  # OK
try:
    print(c.send('q'))
except StopIteration:
    print("Generator zakończył działanie")
