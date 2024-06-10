class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True  # Par défaut, le livre est disponible

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def rendre(self):
        self.disponible = True

    def afficher_info(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"Titre: {self.titre}, Auteur: {self.auteur}, Statut: {statut}"


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = []

    def ajouter_livre(self, livre):
        self.catalogue.append(livre)

    def supprimer_livre(self, livre):
        self.catalogue.remove(livre)

    def afficher_catalogue(self):
        for livre in self.catalogue:
            print(livre.afficher_info())


# Utilisation des classes Livre et Bibliotheque
livre1 = Livre("1984", "George Orwell")
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
livre3 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling")

bibliotheque = Bibliotheque("Bibliothèque Municipale")

# Ajouter des livres à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Afficher le catalogue de la bibliothèque
print("Catalogue de la bibliothèque :")
bibliotheque.afficher_catalogue()

# Emprunter un livre
print("\nEmprunt du livre '1984' :")
if livre1.emprunter():
    print("Le livre '1984' a été emprunté avec succès.")
else:
    print("Le livre '1984' n'est pas disponible.")

# Afficher le catalogue de la bibliothèque après emprunt
print("\nCatalogue de la bibliothèque après emprunt :")
bibliotheque.afficher_catalogue()

# Rendre un livre
print("\nRetour du livre '1984' :")
livre1.rendre()
print("Le livre '1984' a été rendu.")

# Afficher le catalogue de la bibliothèque après retour
print("\nCatalogue de la bibliothèque après retour :")
bibliotheque.afficher_catalogue()
