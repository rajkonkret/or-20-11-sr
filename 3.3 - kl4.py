from pprint import pprint


class Contact:
    all_contacts = []  # pusta lista, wspolna lista dla obiektów

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.name!r} {self.email!r}'


class Suplier(Contact):
    """
    Dziedziczy po klasie contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Krzys", "zenek@onet.pl")
c4 = Contact("Arek", "admin4@wp.pl")
print(c1)  # Adam admin@wp.pl -? po dodaniu w repr !r -> 'Adam' 'admin@wp.pl'
print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl,
# Krzys zenek@onet.pl, Arek admin4@wp.pl]
print(c1.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl,
#  Krzys zenek@onet.pl, Arek admin4@wp.pl]
s1 = Suplier("Tomasz", "tomasz@wp.pl")
print(s1)  # Tomasz tomasz@wp.pl
print(s1.all_contacts)
s1.order("kawa")  # kawa zamówiono od Tomasz
pprint(c1.all_contacts)
