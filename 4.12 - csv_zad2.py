import csv

filename = 'plik_dane.csv'

fields = []
rows = []

with open(filename, mode="r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    print(dialect.quotechar)
    csv_f.seek(0)  # ustawienie odczytu na początek
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(fields)
print(rows)