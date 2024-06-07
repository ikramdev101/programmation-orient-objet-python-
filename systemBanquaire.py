class CompteBancaire:
    def _init_(self, id, titulaire, solde_initial):
        self.id = id
        self.titulaire = titulaire
        self.solde = solde_initial
        self.historique = []

    def deposer(self, montant):
        self.solde += montant
        self.historique.append(f"Dépôt de {montant} FCFA")

    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            self.historique.append(f"Retrait de {montant} FCFA")
        else:
            print("Solde insuffisant")

    def consulter_solde(self):
        print(f"Solde du compte {self.id} de {self.titulaire}: {self.solde} FCFA")

    def consulter_historique(self):
        print(f"Historique des transactions du compte {self.id} de {self.titulaire}:")
        for transaction in self.historique:
            print(transaction)


class Banque:
    def _init_(self, nom):
        self.nom = nom
        self.comptes = []

    def ajouter_compte(self, compte):
        self.comptes.append(compte)
        print(f"Le compte {compte.id} de {compte.titulaire} a été ajouté à la banque {self.nom}")

    def transfert(self, compte_source_id, compte_dest_id, montant):
        compte_source = self.trouver_compte_par_id(compte_source_id)
        compte_dest = self.trouver_compte_par_id(compte_dest_id)
        if compte_source and compte_dest:
            if compte_source.solde >= montant:
                compte_source.retirer(montant)
                compte_dest.deposer(montant)
                print(f"Transfert de {montant} FCFA effectué avec succès de {compte_source.id} vers {compte_dest.id}")
            else:
                print("Solde insuffisant pour effectuer le transfert")
        else:
            print("Compte source ou compte destinataire introuvable")

    def afficher_comptes(self):
        print(f"Liste des comptes de la banque {self.nom}:")
        for compte in self.comptes:
            compte.consulter_solde()

    def trouver_compte_par_id(self, id):
        for compte in self.comptes:
            if compte.id == id:
                return compte
        return None


if __name__ == "_main_":
    
    ma_banque = Banque("Ma Banque")

    compte1 = CompteBancaire(1, "Alice", 1000.0)
    compte2 = CompteBancaire(2, "Bob", 2000.0)
    compte3 = CompteBancaire(3, "Charlie", 3000.0)

    ma_banque.ajouter_compte(compte1)
    ma_banque.ajouter_compte(compte2)
    ma_banque.ajouter_compte(compte3)

    compte1.deposer(500)
    compte2.retirer(300)
    ma_banque.transfert(3, 1, 1000)

    ma_banque.afficher_comptes()
    for compte in [compte1, compte2, compte3]:
        compte.consulter_historique()