from pprint import pprint


class ContactList(list['Contact']):

    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    all_contacts = ContactList()  # pusta lista, wspolna lista dla obiektów

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.name!r} {self.email!r} '


class Suplier(Contact):
    """
    Dziedziczy po klasie contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

    def __repr__(self):
        return "suplier"


# dziedziczaca po Contact
class Friend(Suplier, Contact):  # wielodziedziczenie
    """
    Dziedziczy po kalsie Contact
    """

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def order(self, order):
        print("To jest metoda z klasy Friend")
        Suplier.order(self, order)

    def __repr__(self):
        return f" {self.__class__.__name__}: {self.name!r}, {self.email!r}, +48 {self.phone!r}"


c1 = Contact("Adam", "adam@orange.pl")
print(c1.all_contacts)  # ['Adam' 'adam@orange.pl']

s = Suplier("Radek", "radek@wp.pl")
print(s)
print(s.all_contacts)  # ['Adam' 'adam@orange.pl', 'Radek' 'radek@wp.pl']
s.order("kawa")  # kawa zamówiono od Radek

print(s.all_contacts.search('Adam'))
c2 = Contact("Adam", "kontak_adam@wp.pl")
print(s.all_contacts.search('Adam'))  # ['Adam' 'adam@orange.pl', 'Adam' 'kontak_adam@wp.pl']

contact_list = ContactList()
contact_list.append(c1)
print(contact_list)  # ['Adam' 'adam@orange.pl']

f1 = Friend("Jarek", "jarek@wp.pl", "505678987")
print(f1)  # 'Jarek', 'jarek@wp.pl', +48 '505678987'
print(c1.all_contacts)
# ['Adam' 'adam@orange.pl', 'Radek' 'radek@wp.pl',
# 'Adam' 'kontak_adam@wp.pl', 'Jarek', 'jarek@wp.pl', +48 '505678987']
f1.order("herbata")  # herbata zamówiono od Jarek
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
