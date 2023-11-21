# slownik - para klucz - wartość
# json -> {"name" : "Radek"}
# słownik {'name' : 'Radek'}
# klucze nie mogą sie powtarzać

slownik = {}  # pusty słownik
print(type(slownik))  # <class 'dict'>
print(slownik)  # {} wyświetlenie pustego słownik

slownik['imie'] = "Radek"
print(slownik)  # {'imie': 'Radek'}
slownik.update({"wiek": 39})
print(slownik)  # {'imie': 'Radek', 'wiek': 39}

print(slownik['imie'])  # Radek

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 39])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

# print(slownik['Radek']) # KeyError: 'Radek'
print(slownik.get('Radek', "Radek to nie klucz"))  # Radek to nie klucz
