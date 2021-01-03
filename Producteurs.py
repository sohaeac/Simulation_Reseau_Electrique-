import time

class Producteur:

    def __init__(self, type_centrale, nom, production, prix_combustible, co2):
        self.type_centrale = type_centrale
        self.nom = nom
        self.production = production
        self.prix_combustible = prix_combustible
        self.co2 = co2

    def energie_produite(self,production):
        return production

    def cout_production(self, production, prix_combustible):
        cout_total = production*prix_combustible
        return (cout_total)

    def production_CO2(self, co2):
        pass


class CentralGaz(Producteur):
    def __str__(self): 
        return("  Type de central: {}\n  Nom de la central: {}\n  Production :{} kWh\n  Prix de production :{}€\n  Production de CO2:{} kg".format(self.type_centrale, self.nom, Producteur.energie_produite(self,self.production),Producteur.cout_production(self,self.production, self.prix_combustible),self.co2))

class CentralNucleaire(Producteur):
    
    def Action(self, action):
        if action == "Demarrer":
            init = self.production
            self.production = 0
            print("La centrale démarre tout doucement...")
            time.sleep(5)
            self.production = init
        elif action == "Arreter":
            pass

    def __str__(self):
        return("  Type de central: {}\n  Nom de la central: {}\n  Production :{} kWh\n  Prix de production :{}€\n  Production de CO2:{} kg".format(self.type_centrale, self.nom, Producteur.energie_produite(self,self.production),Producteur.cout_production(self,self.production, self.prix_combustible),self.co2))
        

class ParcEolien(Producteur):
    def __init__(self, type_centrale, nom, production, prix_combustible, co2, meteo):
        Producteur.__init__(self, type_centrale, nom, production, prix_combustible, co2)
        self.production = production
        self.meteo = meteo
        if self.meteo == "vent":
            self.production += 10
    def __str__(self):
       return("  Type de central: {}\n  Nom de la central: {}\n  Production :{} kWh\n  Prix de production :{}€\n  Production de CO2:{} kg".format(self.type_centrale, self.nom, Producteur.energie_produite(self,self.production),Producteur.cout_production(self,self.production, self.prix_combustible),self.co2))

class CentraleSolaire(Producteur):
    def __init__(self,type_centrale, nom, production, prix_combustible, co2, meteo):
        Producteur.__init__(self, type_centrale, nom, production, prix_combustible, co2)
        self.production = production
        self.meteo = meteo
        if self.meteo == "soleil":
            self.production += 10
    def __str__(self):
        return("  Type de central: {}\n  Nom de la central: {}\n  Production :{} kWh\n  Prix de production :{}€\n  Production de CO2:{} kg".format(self.type_centrale, self.nom, Producteur.energie_produite(self,self.production),Producteur.cout_production(self,self.production, self.prix_combustible),self.co2))

class AchatElectricite(Producteur):
    def __init__(self, production):
        self.production = production
    def __str__(self):
        return("  Achat de {} kWh".format(self.production))


