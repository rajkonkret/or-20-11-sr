import pickle
from kl10 import Person

with open('dane.pickle', 'rb') as file:
    p = pickle.load(file)

print("--------")
print(p)
print(type(p))
print(p[0])
print(type(p[0]))  # <class 'kl10.Person'>

for person in p:
    print(f"id={person.id}, first_name={person.first_name}, last_name={person.last_name}")
    person.greets()
