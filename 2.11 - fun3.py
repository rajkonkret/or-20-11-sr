# ** argumenty słownikowe
def example(a, b, /, d=0, **kwargs):
    print(a, b, d)
    print(kwargs)
    return a * b


print(example(1, 2))
print(type(example))  # <class 'function'>
print(example.__code__.co_varnames)  # ('a', 'b', 'd', 'kwargs')
# print(example(b=7, a=7))  # TypeError: example() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela argument,
# które musza byc podane po pozycji od argumentów, ktore mogą byc podane po nazwie
print(example(1, 2, 3))  # 1 2 3
print(example(1, 2, 3, e=9))  # {'e': 9}
print(example(1, 2, d=8, e=9))  # {'e': 9}
print(example(1, 2, 3, e=9, a=8))  # {'e': 9, 'a': 8}
