class Consommateur():
    def __init__(self, type_consommateur, nom, consommation):
        self.type_consommateur = type_consommateur
        self.nom = nom
        self.consommation = consommation

class Ville(Consommateur):
    def __str__(self):
        return("  Type de consommateur: {} \n  Nom: {}\n  Consommation: {} kWh".format(self.type_consommateur, self.nom, self.consommation))

class Entreprise(Consommateur):
    def __str__(self):
        return("  Type de consommateur: {} \n  Nom: {}\n  Consommation: {} kWh".format(self.type_consommateur, self.nom, self.consommation))

class VenteElecEtranger(Consommateur):
    pass

class Dissipateur(Consommateur):
    pass
