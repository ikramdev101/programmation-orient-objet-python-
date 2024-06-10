# Classe de base Vehicule
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def afficher_details(self):
        return f"Marque: {self.marque}, Modèle: {self.modele}"

# Classe Electrique
class Electrique:
    def __init__(self, autonomie):
        self.autonomie = autonomie

    def afficher_autonomie(self):
        return f"Autonomie: {self.autonomie} km"

# Classe Thermique
class Thermique:
    def __init__(self, capacite_reservoir):
        self.capacite_reservoir = capacite_reservoir

    def afficher_capacite_reservoir(self):
        return f"Capacité du réservoir: {self.capacite_reservoir} litres"

# Classe VoitureElectrique qui hérite de Vehicule et Electrique
class VoitureElectrique(Vehicule, Electrique):
    def __init__(self, marque, modele, autonomie):
        Vehicule.__init__(self, marque, modele)
        Electrique.__init__(self, autonomie)

    def afficher_details_complets(self):
        details_vehicule = self.afficher_details()
        details_autonomie = self.afficher_autonomie()
        return f"{details_vehicule}, {details_autonomie}"

# Classe VoitureThermique qui hérite de Vehicule et Thermique
class VoitureThermique(Vehicule, Thermique):
    def __init__(self, marque, modele, capacite_reservoir):
        Vehicule.__init__(self, marque, modele)
        Thermique.__init__(self, capacite_reservoir)

    def afficher_details_complets(self):
        details_vehicule = self.afficher_details()
        details_reservoir = self.afficher_capacite_reservoir()
        return f"{details_vehicule}, {details_reservoir}"

# Créer des instances de VoitureElectrique et VoitureThermique
voiture_electrique = VoitureElectrique("Tesla", "Model S", 600)
voiture_thermique = VoitureThermique("Toyota", "Corolla", 50)

# Utiliser les méthodes pour afficher les informations
print(voiture_electrique.afficher_details_complets())
print(voiture_thermique.afficher_details_complets())
