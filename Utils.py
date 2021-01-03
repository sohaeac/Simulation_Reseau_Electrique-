import random
import Producteurs, Consommateurs, Meteo

def ListeProducteurs():
    global production_totale

    ''' FORMAT:
    CentralNucleaire("type_centrale", "nom", production, prix_combustible, consommation_CO2)
    CentralGaz("type_centrale","nom", production, prix_combustible, CO2)
    ParcEolien("type_centrale","nom", production, prix_combustible, CO2, meteo)
    '''
    # RAJOUTER ICI LES CENTRALES (ensuite les insérer dans listeCentrales)

    production_rand = random.randint(1,10)
    CentralNucleaire1= Producteurs.CentralNucleaire("Centrale Nucléaire","Nuke 2000", 10 , 10, 500)
    CentralGas1 = Producteurs.CentralGaz("Centrale au gaz", "Gas 1506", production_rand , 10, 500)
    ParcEolien = Producteurs.ParcEolien("Parc Eolien","EolienParc 2033", 13, 40, 20, Meteo.meteo())
    CentraleSolaire = Producteurs.CentraleSolaire("Centrale Solaire","SolarParc 33", 20, 30, 20, Meteo.meteo())
    Achat = Producteurs.AchatElectricite(200)


    listeCentrales = [CentralNucleaire1, CentralGas1, ParcEolien, CentraleSolaire, Achat]
    
    print("  ######################")
    print("  #LISTE DE PRODUCTEURS#")
    print("  ######################")
    x = '\n'
    print(x)
    
    for i, central in enumerate(listeCentrales):
        print("[{}]".format(i+1))
        print(central)
        print("----------------------------------")
    

    production_totale = 0
    for central in listeCentrales:
        production_totale += central.production

    print("PRODUCTION TOTALE: {} kWh".format(production_totale))
    return (" ")

def ListeConsommateurs():
    global consommation_totale

    print("  ########################")
    print("  #LISTE DE CONSOMMATEURS#")
    print("  ########################")
    x = '\n'
    print(x)
    ville_rand = random.randint(250,300)
    entreprise_rand = random.randint(1,10)

    #RAJOUTER ICI LES CONCOMMATEURS (ensuite les insérer dans listeConsommateurs)
    #Format: Consommateurs.Ville("type_consommateur", "nom_ville", consommation)
    conso1 = Consommateurs.Ville("Ville", "Madrid", ville_rand)
    conso2 = Consommateurs.Entreprise("Entreprise", "Shop S.A", entreprise_rand)
    
    global listeConsommateurs
    listeConsommateurs = [conso1, conso2]

    for i, conso in enumerate(listeConsommateurs):
        print("[{}]".format(i+1))
        print(conso)
        print("----------------------------------")
    

    consommation_totale = 0
    for conso in listeConsommateurs:
        consommation_totale += conso.consommation
    print("CONSOMMATION TOTAL TOTALE: {} kWh".format(consommation_totale))
    return(" ")

def MessageAlerte():
    print("  ###################")
    print("  #MESSAGES D'ALERTE#")
    print("  ###################")
    print("")
    if production_totale > consommation_totale:
        print("ATTENTION: Surproduction! Pensez à stocker et vendre l'énergie")
    if production_totale < consommation_totale:
        print("ATTENTION: Manque de production! Pensez à acheter de l'énergie!")
    return('')

