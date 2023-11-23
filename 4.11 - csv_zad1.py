# csv - plik tekstowy, dane oddzielone znakiem podziału
# zenek, Marek, tomek

import csv

# csv - biblioteka do plików csv
fields = ['name', 'branch', 'year', 'cgpa']

dict_list = [
    {'name': 'radek', 'branch': 'coe', "year": 3, 'cgpa': "0"},
    {'name': 'marek', 'branch': 'cos', "year": 4, 'cgpa': "1"},
    {'name': 'zenek', 'branch': 'cot', "year": 2, 'cgpa': "2"},
    {'name': 'jhon', 'branch': 'col', "year": 1, 'cgpa': "3"},
]
# newline - eliminacja pustej linii
with open('plik_dane.csv', 'w', newline='') as csv_f:
    cswriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=":")
    # delimiter= znak oddzielający
    cswriter.writeheader()
    cswriter.writerows(dict_list)
