# __missing__ - metoda wykonywana gdy nie ma klucza w słowniku
# dziedziczenie

class DefaultDict(dict):  # dict - słownik
    def __missing__(self, key):
        return "default"


class AutoKeydict(dict):
    def __missing__(self, key):
        self[key] = 0


# tak zmodyfikowac __mising__ by kluc zmogłbyc podany bez zachowania duze małe litery
# name - . NAme


class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        # return self[key.lower()]
        if isinstance(key, str):
            return self.get(key.lower())


d_python = {}
d_python['name'] = 'Radek'
print(d_python)  # {'name': 'Radek'}
print(d_python['name'])
# print(d_python['imie'])  #  KeyError: 'imie'

d1 = DefaultDict()
d1['name'] = "Radek"
print(d1['name'])
print(d1['imie'])  # default

d2 = AutoKeydict()
print(d2['imie'])
print(d2)  # {'imie': 0}

d3 = CaseInsensitiveDict()
d3['name'] = "Radek"
print(d3['NAME'])  # Radek

d3[4] = "Polska"
print(d3)
print(d3[4])  # Polska
d_python[4] = "TY"
print(d_python)  # {'name': 'Radek', 4: 'TY'}
print(d_python[4])
d_python[(3,)] = 0
print(type(d_python))  # <class 'dict'>
