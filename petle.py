# for - petla iteracyjna

for i in range(10):
    print(i)

for i in range(10):
    for j in range(10):
        print(i, j)

lista2 = [j for j in range(6)]
print(lista2)  # [0, 1, 2, 3, 4, 5]

for c in lista2:
    print(c)

# if - warunek
# if warunek:
#   operacja gdy warunek poprawny (True)
# else:
#   w przecinym przypadku

# a = 1
a = 2
if a == 1:
    print(f"A równa się 1")
else:
    print(f"A nie równa się 1")
# A równa się 1 dla a = 1
# A nie równa się 1 a = 2

if a == 1:
    print("A równa się 1")
elif a == 2:
    print("A równa się 2")
elif a == 3:
    print("A równa się 3")
else:
    print("A nie jest 1 ani 2")

if a > 0:
    print("A > 0")
elif a > 10:
    print("A > 10")
