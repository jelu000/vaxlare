import os
import vaxla


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-Växlare-\n")

    pris = input("\tMata in pris på varan i kr: ")
    inbet = input("\tMata in inbetalt pelopp i kr: ")

    exChange(int(pris), int(inbet))


def exChange(priset, inbetalning):
    
    antal_mynt = 0
    pengar_tillbaka = 0

    sedlar_mynt_dictonary = {500:0, 100:0, 50:0, 20:0, 10:0, 5:0, 1:0}

    if priset > inbetalning:
        print("\n\tFattas Pengar! ")
    
    else:
        
        #500----------------------------------------
        antal_mynt = vaxla.exchange500(inbetalning)
        
        if  antal_mynt > 0:
            sedlar_mynt_dictonary[500] = antal_mynt 
            pengar_tillbaka = (inbetalning - priset) % 500

            #print("Pengar tillbaka = " + str(pengar_tillbaka))
        
        #100----------------------------------------
        antal_mynt = vaxla.exchange100(pengar_tillbaka)
        if  antal_mynt > 0:
            sedlar_mynt_dictonary[100] = antal_mynt 
            pengar_tillbaka = pengar_tillbaka % 100

            #print("Pengar tillbaka = " + str(pengar_tillbaka))
        
        #50----------------------------------------
        antal_mynt = vaxla.exchange50(pengar_tillbaka)
        if  antal_mynt > 0:
            sedlar_mynt_dictonary[50] = antal_mynt 
            pengar_tillbaka = pengar_tillbaka % 50

        #print("Pengar tillbaka = " + str(pengar_tillbaka))
        
        #20----------------------------------------
        antal_mynt = vaxla.exchange20(pengar_tillbaka)
        if  antal_mynt > 0:
            sedlar_mynt_dictonary[20] = antal_mynt 
            pengar_tillbaka = pengar_tillbaka % 20

        #print("Pengar tillbaka = " + str(pengar_tillbaka))

        #10----------------------------------------
        antal_mynt = vaxla.exchange10(pengar_tillbaka)
        if  antal_mynt > 0:
            sedlar_mynt_dictonary[10] = antal_mynt 
            pengar_tillbaka = pengar_tillbaka % 10

        #print("Pengar tillbaka = " + str(pengar_tillbaka))

        #5----------------------------------------
        antal_mynt = vaxla.exchange5(pengar_tillbaka)
        if  antal_mynt > 0:
            sedlar_mynt_dictonary[5] = antal_mynt 
            pengar_tillbaka = pengar_tillbaka % 5

        #print("Pengar tillbaka = " + str(pengar_tillbaka))

        #1----------------------------------------
        antal_mynt = vaxla.exchange1(pengar_tillbaka)
        if  antal_mynt > 0:
            sedlar_mynt_dictonary[1] = antal_mynt 
            pengar_tillbaka = pengar_tillbaka % 1

        #print("Pengar tillbaka = " + str(pengar_tillbaka))   

        print("\n\t----------------------------------------")
        print("\tVäxel tillbaka!\n")
        print("\tAntal 500 lappar: " + str(sedlar_mynt_dictonary[500]))
        print("\tAntal 100 lappar: " + str(sedlar_mynt_dictonary[100]))
        print("\tAntal 50 lappar: " + str(sedlar_mynt_dictonary[50]))
        print("\tAntal 20 lappar: " + str(sedlar_mynt_dictonary[20]))
        print("\tAntal 10 kronor: " + str(sedlar_mynt_dictonary[10]))
        print("\tAntal 5 kronor: " + str(sedlar_mynt_dictonary[5]))
        print("\tAntal 1 kronor: " + str(sedlar_mynt_dictonary[1]) + "\n\n")


        #print("test = " + str(sedlar_mynt_dictonary))
    
    
main()