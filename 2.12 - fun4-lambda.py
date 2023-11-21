# lambda - skrócony zapis funkcji
# mozliwosc zdeklarowania funkcji w miejscu wykonania

def liczymy(x, y):
    return x * y


print(liczymy(4, 5))

liczymy2 = lambda x, y: x * y  # lambda ma return
print(liczymy2(100, 200))  # 20000

lista = [1, 2, 3, 4, 5, 6, 7, 20, 55, 100, 123]

lista2 = []
for i in lista:
    lista2.append(i * 2)

print(lista2)  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
print([i * 2 for i in lista])  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]


def zmien(x):
    return x * 2


# map() - mapowanie, pobiez kolejne elementy z kolekcji, wykonaj zadanie przekazane w formie funkcji
print(f"Użycie map() {list(map(zmien, lista))}")
# Użycie map() [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
print(f"Użycie map() {list(map(lambda x: x * 2, lista))}")
print(f"Użycie map() {list(map(lambda x: x * 5, lista))}")
print(f"Użycie map() {list(map(lambda x: x / 20, lista))}")
print(f"Użycie map() {list(map(lambda x: x + 2, lista))}")
# Użycie map() [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
# Użycie map() [5, 10, 15, 20, 25, 30, 35, 100, 275, 500, 615]
# Użycie map() [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 1.0, 2.75, 5.0, 6.15]
# Użycie map() [3, 4, 5, 6, 7, 8, 9, 22, 57, 102, 125]
# funkcja lambda użyta jako funkcja anonimowa
# 14:30

# filter() - filtruje dane wg zadanej funkcji
print(f"Użycie filter(): {list(filter(lambda x: x < 5, lista))}")
# Użycie filter(): [1, 2, 3, 4]
# x > 8
# x >3 i x <20
print(f"Użycie filter(): {list(filter(lambda x: x > 8, lista))}")
# Użycie filter(): [20, 55, 100, 123]
print(f"Użycie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")
# x > 3 and x < 20 -> 3 < x < 20
# Użycie filter(): [4, 5, 6, 7]

r0 = {'miasto': "Kielce"}
r1 = {'miasto': 'Kielce', 'ZIP': '25-900'}
print(r0['miasto'])
print(r1['miasto'])
print(r1['ZIP'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

d_zip = lambda row: row.setdefault('ZIP', '00-000')
print(d_zip(r0))  # 00-000
print(d_zip(r1))  # 25-900
print(r0)  # {'miasto': 'Kielce', 'ZIP': '00-000'}
print(r1)  # {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.97), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
# c[1], c -> (33.12,(2001, 33.12))
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)
print(lata)  # [(2000, 29.97), (2001, 33.12), (2010, 32.92)]
