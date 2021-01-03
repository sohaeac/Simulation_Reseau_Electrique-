import Producteurs, Consommateurs, Utils 
import sched, time
from os import system, name 
from time import sleep 
s = sched.scheduler(time.time, time.sleep)

def clear(): 
    
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

def Interface(sc):
    print("                           --------- SIMULATION RESEAU ELECTRIQUE ---------")
    
    print(Utils.ListeProducteurs())
    print("----------------------------------------------------------------------------------------------------------------------------")
    print(Utils.ListeConsommateurs())
    print("----------------------------------------------------------------------------------------------------------------------------")
    print(Utils.MessageAlerte())
    
    s.enter(1, 1, Interface, (sc,))
    time.sleep(2)
    clear()


def menu():
    print("")

    a = """
    ▒█▀▀▀█ ▀█▀ ▒█▀▄▀█ ▒█░▒█ ▒█░░░ ░█▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ 
    ░▀▀▀▄▄ ▒█░ ▒█▒█▒█ ▒█░▒█ ▒█░░░ ▒█▄▄█ ░▒█░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ 
    ▒█▄▄▄█ ▄█▄ ▒█░░▒█ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ░▒█░░ ▄█▄ ▒█▄▄▄█ ▒█░░▀█ 
                                            by Sohaib & Achrafe
    """
    print(a)
    print("")

    print("    [1] Montrer simulation")
    print("")
    print("    [0] Quiter simulation")
    print("")

menu()
option = int(input("Choisir option:  "))

while option != 0:
    if option == 1:
        s.enter(1, 1, Interface, (s,))
        s.run()
    else:
        clear()
        print("Option invalid")
    menu()
    option = int(input("Choisir option: \n"))

