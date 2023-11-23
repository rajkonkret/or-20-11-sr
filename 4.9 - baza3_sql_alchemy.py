# sql alchemy
from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)
# pip instal sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///:memory:')  # baza danych w pamięci
Base = declarative_base()


class Person(Base):  # klasa jako encja
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship('Address',
                             back_populates='person',
                             order_by="Address.email",
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name}(id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship('Person', back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
ssesion = Session()

anakin = Person(name='Anakin', age=38)
obi = Person(name="Obi", age=40)
obi.addresses = [
    Address(email='obi@example.com'),
    Address(email='waka@example.com'),
]

ssesion.add(anakin)
ssesion.add(obi)
ssesion.commit()

all_ = ssesion.query(Person).all()
print(all_)  # [Anakin(id=1), Obi(id=2)]

an1 = ssesion.query(Person).first()
print(an1)  # Anakin(id=1)
print(type(an1))  # <class '__main__.Person'>
print(an1.id, an1.name, an1.age)  # 1 Anakin 38

obi1 = ssesion.query(Person).filter(
    Person.name.like('Obi%')
).first()

print(obi1)  # Obi(id=2)
print(obi1.addresses)  # [obi@example.com, waka@example.com]
# 13:55
