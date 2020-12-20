#moment04-c
#Arvid Anderson TE19D
""" Jag har valt att använda mig utav en try och except för att enkelt kunna få en input igen om det inte är ett heltal som är inmatat. If och else
för att kunna avgöra och ändra om inputen"""



import subprocess
import platform
import time
def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)



global s1minne
global s2minne
global areaminne
global kvadratminne
s1minne = []
s2minne = []
areaminne = []
kvadratminne = []

#antal ggr funktionen körs
antalggr = 0

def uppgift1():
    # gör till global lägger till 1 varje gång funktionen körs
    global antalggr
    antalggr+=1

    #Mina inputs
    s1 = int(input("Ange ena sidan på rektangeln: "))
    s1minne.append(s1)
    s2 = int(input("Ange andra på rektangeln: "))
    s2minne.append(s2)

    #Area = b * h
    area = s1 * s2
    areaminne.append(s1 * s2)
    #Printar ut arean
    print(f"Arean på rektangeln är {area}")

    #if else
    if s1 == s2:
        print(f"Rektangeln har sidorna {s1} och {s2} detta betyder att det är en kvadrat eftersom sidorna är lika långa")
        kvadratminne.append("Ja")
    else:
        print(f"Rektangeln har sidorna {s1} och  {s2}")
        kvadratminne.append("Nej")

    #Uppgift c
    while True:
        try:
            volymantal = int(input("Mata in höjd: "))
            break
        except:
            print("Det är inget heltal! Försök igen")
    
    if volymantal < 0:
        volymantal = 1+1
    else:
        pass
    if volymantal > 10:
        volymantal = 10+1
    else:
        pass

    #Formatting
    print('{:^10}'.format('Höjden  Volymen'))
    print('{:^10}'.format('---------------'))

    #for loop
    for i in range(1,volymantal):
        #Stora volymen i variablen
        volymen = s1 * s2 * i
        #Print
        print('{:2}'.format(i) + '{:>10}'.format(volymen))
    #Formatting
    print('{:^10}'.format('---------------'))
    


while True:
    svar = str(input("Vill du utföra en beräkning Y/N: "))
    if svar == "Y":
        uppgift1() 
    else:
        #Rensar skärmmen
        clear()
        #Sleep en sekund annars är datorn för snabb och rensar printen
        time.sleep(1)
        #For loop som visar beräkningarna
        print("Beräkningar:")
        print(" ")
        for i in range(antalggr):
            print("--------------")
            # i + 1 för att det ska se bra ut och siffran ska börja på 1 istället för 0
            print(f"Beräkning {i + 1}")
            print(f"Först sidan: {s1minne[i]} cm")
            print(f"Andra sidan: {s2minne[i]} cm")
            print(f"Arean: {areaminne[i]} cm2")
            print(f"Kvadrat: {kvadratminne[i]}")
            print("--------------")
            print(" ")
        #Slutar programmet
        break
