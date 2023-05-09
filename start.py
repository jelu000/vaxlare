import os
import vaxla


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-Växlare-\n")

    pris = input("\tMata in pris på varan i kr: ")
    inbet = input("\tMata in inbetalt pelopp i kr: ")
    #anropar växlings funktion
    exChangeNow(int(pris), int(inbet))

#definerar växlingsdunktion som skriver ut växling
def exChangeNow(priset, inbetalning):
    
    if priset > inbetalning:
        print("\n\tFattas Pengar! ")

    else:
        vaxel_tillbaka_dictonary = vaxla.get_exchange_dict(inbetalning, priset)
        
        print("\n\t----------------------------------------")
        print("\tVäxel tillbaka:\n")
        print("\tAntal 500 lappar: " + str(vaxel_tillbaka_dictonary[500]))
        print("\tAntal 100 lappar: " + str(vaxel_tillbaka_dictonary[100]))
        print("\tAntal 50 lappar: " + str(vaxel_tillbaka_dictonary[50]))
        print("\tAntal 20 lappar: " + str(vaxel_tillbaka_dictonary[20]))
        print("\tAntal 10 kronor: " + str(vaxel_tillbaka_dictonary[10]))
        print("\tAntal 5 kronor: " + str(vaxel_tillbaka_dictonary[5]))
        print("\tAntal 1 kronor: " + str(vaxel_tillbaka_dictonary[1]) + "\n\n")

        print("test = " + str(vaxel_tillbaka_dictonary))


main()