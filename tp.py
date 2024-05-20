
### Exemple 1 : Classe de Base et Instanciation


class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def demarrer(self):
        print(f"{self.marque} {self.modele} démarre.")

# Instanciation de la classe Voiture
ma_voiture = Voiture("Toyota", "Corolla", 2020)
print(ma_voiture.marque)  # Output: Toyota
ma_voiture.demarrer()  # Output: Toyota Corolla démarre.


### Exemple 2 : Héritage


class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def demarrer(self):
        print(f"{self.marque} {self.modele} démarre.")

class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, annee, autonomie):
        super().__init__(marque, modele, annee)
        self.autonomie = autonomie
    
    def recharger(self):
        print(f"{self.marque} {self.modele} est en charge.")

# Instanciation de la classe VoitureElectrique
ma_voiture_elec = VoitureElectrique("Tesla", "Model 3", 2021, 500)
print(ma_voiture_elec.marque)  # Output: Tesla
ma_voiture_elec.demarrer()  # Output: Tesla Model 3 démarre.
ma_voiture_elec.recharger()  # Output: Tesla Model 3 est en charge.


### Exemple 3 : Encapsulation

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.__titulaire = titulaire
        self.__solde = solde
    
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"{montant} déposé. Solde actuel : {self.__solde}")
    
    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            print(f"{montant} retiré. Solde actuel : {self.__solde}")
        else:
            print("Fonds insuffisants.")

    def afficher_solde(self):
        print(f"Solde de {self.__titulaire} : {self.__solde}")

# Instanciation de la classe CompteBancaire
mon_compte = CompteBancaire("Alice")
mon_compte.deposer(100)
mon_compte.retirer(50)
mon_compte.afficher_solde()


### Exemple 4 : Polymorphisme


class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Woof!"

class Chat(Animal):
    def parler(self):
        return "Meow!"

def faire_parler(animal):
    print(animal.parler())

# Instanciation des classes Chien et Chat
mon_chien = Chien()
mon_chat = Chat()

faire_parler(mon_chien)  # Output: Woof!
faire_parler(mon_chat)  # Output: Meow!


### Exemple 5 : Méthodes et Attributs de Classe


class Compteur:
    nombre_instances = 0
    
    def __init__(self):
        Compteur.nombre_instances += 1
    
    @classmethod
    def afficher_nombre_instances(cls):
        print(f"Nombre d'instances : {cls.nombre_instances}")

# Instanciation de la classe Compteur
c1 = Compteur()
c2 = Compteur()
Compteur.afficher_nombre_instances()  # Output: Nombre d'instances : 2


### Exemple 6 : Utilisation de Propriétés


class Rectangle:
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self, valeur):
        if valeur > 0:
            self.__largeur = valeur
        else:
            raise ValueError("La largeur doit être positive.")
    
    @property
    def hauteur(self):
        return self.__hauteur
    
    @hauteur.setter
    def hauteur(self, valeur):
        if valeur > 0:
            self.__hauteur = valeur
        else:
            raise ValueError("La hauteur doit être positive.")
    
    @property
    def aire(self):
        return self.__largeur * self.__hauteur

# Instanciation de la classe Rectangle
mon_rectangle = Rectangle(10, 20)
print(mon_rectangle.aire)  # Output: 200
mon_rectangle.largeur = 15
print(mon_rectangle.aire)  # Output: 300


