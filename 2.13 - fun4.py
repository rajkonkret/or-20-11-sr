# napisanie funkcji  ktora za pomoca prekazanych argumentów
# stworzy słownik i zwroci go
# first, last, age=None

def build_person(first, name, age=None):
    person = {'first': first, 'name': name}
    if age:  # dla None warunek jest False
        person['age'] = age

    return person


while True:
    print("Podaj imie i nazwisko")
    print("Wpisz q by zakonczyc")
    f_name = input("Imię: ")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break
    age = input("wiek: ")
    if age == 'q':
        break

    print(build_person(f_name, l_name, age))
