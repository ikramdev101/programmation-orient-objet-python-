class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je suis un animal nommé {self.nom} et j'ai {self.age} ans."

    def crier(self):
        raise NotImplementedError("Cette méthode doit être redéfinie par les sous-classes")

class Mammifere(Animal):
    def __init__(self, nom, age, nombre_pattes):
        super().__init__(nom, age)
        self.nombre_pattes = nombre_pattes

    def se_presenter(self):
        return f"Je suis un mammifère nommé {self.nom} et j'ai {self.age} ans avec {self.nombre_pattes} pattes."

class Chien(Mammifere):
    def __init__(self, nom, age):
        super().__init__(nom, age, 4)

    def se_presenter(self):
        return f"Je suis un chien nommé {self.nom} et j'ai {self.age} ans avec {self.nombre_pattes} pattes."

    def crier(self):
        return "Woof! Woof!"

class Chat(Mammifere):
    def __init__(self, nom, age):
        super().__init__(nom, age, 4)

    def se_presenter(self):
        return f"Je suis un chat nommé {self.nom} et j'ai {self.age} ans avec {self.nombre_pattes} pattes."

    def crier(self):
        return "Miaou! Miaou!"

chien = Chien("Rex", 5)
chat = Chat("Whiskers", 3)

print(chien.se_presenter())
print(chien.crier())

print(chat.se_presenter())
print(chat.crier())
