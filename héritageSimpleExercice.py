# Classe de base Personne
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

# Classe Etudiant qui hérite de Personne
class Etudiant(Personne):
    def __init__(self, nom, age, domaine_etude):
        super().__init__(nom, age)
        self.domaine_etude = domaine_etude

    def etudier(self):
        return f"{self.nom} étudie {self.domaine_etude}."

# Classe Professeur qui hérite de Personne
class Professeur(Personne):
    def __init__(self, nom, age, matiere):
        super().__init__(nom, age)
        self.matiere = matiere

    def enseigner(self):
        return f"{self.nom} enseigne {self.matiere}."

# Créer des instances de Etudiant et Professeur
etudiant1 = Etudiant("Alice", 20, "Informatique")
etudiant2 = Etudiant("Bob", 22, "Mathématiques")

professeur1 = Professeur("Dr. Smith", 45, "Physique")
professeur2 = Professeur("Mme. Johnson", 38, "Chimie")

# Utiliser les méthodes pour afficher les informations
print(etudiant1.se_presenter())
print(etudiant1.etudier())

print(etudiant2.se_presenter())
print(etudiant2.etudier())

print(professeur1.se_presenter())
print(professeur1.enseigner())

print(professeur2.se_presenter())
print(professeur2.enseigner())
