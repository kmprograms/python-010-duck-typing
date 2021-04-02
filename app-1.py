# Mozemy rozroznic nastepujace rodzaje typowania:

# -------------------------------------------------------------------------------------------------------
# DYNAMIC TYPING
# -------------------------------------------------------------------------------------------------------
# Typy sprawdzane sa ale juz kiedy aplikacja dziala.
# Typ zmiennej moze sie zmieniac w trakcie wykonywania aplikacji.
# Python jest jezykiem typowanym dynamicznie.

# Zwroc uwage ze ponizej w pamieci tworzysz miejsce, ktore przechowa wartosc liczbowa 100
# do tego miejsca zaczynasz odwolywac sie poprzez nazwe x
# dzieki temu od teraz mozesz wygodnie uzywajac x odniesc sie do obszaru, ktory przechowuje
# wartosc liczbowa 100
x = 100
# print(type(x))

# Chwile pozniej tworzysz nowy obszar. W tym obszarze przechowany bedzie napis. Teraz
# x staje sie nazwa tego nowego obszaru.
x = 'ala'
# print(type(x))

# Okazuje sie ze x to tylko nazwa. Nie ma przypisanego konkretnego typu. Wskazuje tylko na
# obszar i w momencie kiedy ktos wywola type na rzecz x to odniesie sie do typu obszaru na
# ktory aktualnie wskazuje x. Tak wlasnie dziala dynamic typing

# -------------------------------------------------------------------------------------------------------
# STATIC TYPING
# -------------------------------------------------------------------------------------------------------
# Typy sprawdzane sa juz na etapie kompilacji, jeszcze przed uruchomieniem.
# Przyklady jezykow typowanych statycznie: Java, C++, C#
# W takim mechanizmie typowania zmienna / obiekt nie zmienia typu chyba ze poprzez
# mechanizmy rzutowania
# W Python wprowadzono co prawda type hints ale jak sama nazwa wskazuje to tylko podpowiedzi
# i nie prowadza do tego zeby Python stal sie jezykiem typowanym statycznie


def add(a: int, b: int) -> int:
    return a + b


# print(add(10, 22))
# print(add('10', '22'))

# https://www.youtube.com/watch?v=w5_f0VQnNbc&list=PLCXqHvi_kahzWEUgvd9J3C739Qeuf4WiZ&index=3


# -------------------------------------------------------------------------------------------------------
# DUCK TYPING
# -------------------------------------------------------------------------------------------------------
# IF IT WALKS LIKE A DUCK AND IT QUACKS LIKE A DUCK THEN IT MUST BE A DUCK

# Jest to koncepcja powiazana z dynamicznym typowaniem, gdzie typ lub klasa obiektu
# sa mniej istotne niz metoda lub inny skladnik ktore definiuja
# Podczas stosowania tego podejscia nie sprawdzamy typu. Zamiast tego sprawdzamy
# obecnosc metody lub innego skladnika.

# Zdefiniujmy teraz kilka klas


class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'THIS IS {self.name}'


class Greeting:

    @staticmethod
    def greeting(person: Person):
        print('HELLO!')
        print(person.info())


john = Person('JOHN')
Greeting.greeting(john)


# Ale mozesz teraz zrobic calkiem inna klase i dopoki ma ona w sobie metode info tez
# mozesz ja uzywac w metodzie greeeting


class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def info(self):
        return f'NAME: {self.name} QUANTITY: {self.quantity}'


product = Product('PROD A', 10)
Greeting.greeting(product)


# Ale jezeli zrobimy kolejna klase w ktorej nie bedziemy mieli metody info
# dostaniemy blad


class Message:
    def __init__(self, title, text):
        self.title = title
        self.text = text


# message = Message('TITLE', 'TEXT')
# Greeting.greeting(message)
