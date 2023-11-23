import chardet

with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")
    file.write("Radek2\n")
    file.write("dośdane\n")
    file.write("Zażółć\n")

with open('test.log', 'r') as file:
    data = file.read()

print(data)  # doĹ›dane

with open('test.log', 'r', encoding='utf-8') as file:
    data2 = file.read()

print(data2)  # dośdane

with open('test.log', 'rb') as file:  # wczytujemy bajtowo
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# Przy odpowiednio duzej próbce mamy włsciwa odpowiedz
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
enc = result['encoding']
print(raw_data.decode(encoding=enc))
