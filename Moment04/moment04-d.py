#moment04-d
#Arvid Anderson TE19D

"""
Har redan delvis gjort detta på uppgift C, men har ej sparat ner höjden jag ska räkna upp till i någon lista. Redan lagrat rektangels två sidor i listor

Därför tänker jag använda mig av samma kod och bara enkelt lägga till en till lista som sparar höjden jag ska räkna upp till.

Se kommenterarer i koden, raderat alla kommenterar från uppgift c för lättare att läsa det som var nytt för denna uppgiften

"""

import subprocess
import platform
import time
def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)


#Behöver göra en ny lista för höjdensminne
global s1minne
global s2minne
global areaminne
global kvadratminne
global höjdenminne
s1minne = []
s2minne = []
areaminne = []
kvadratminne = []
höjdenminne = []
antalggr = 0

def uppgift1():
    global antalggr
    antalggr+=1
    s1 = int(input("Ange ena sidan på rektangeln: "))
    s1minne.append(s1)
    s2 = int(input("Ange andra på rektangeln: "))
    s2minne.append(s2)
    area = s1 * s2
    areaminne.append(s1 * s2)
    print(f"Arean på rektangeln är {area}")


    if s1 == s2:
        print(f"Rektangeln har sidorna {s1} och {s2} detta betyder att det är en kvadrat eftersom sidorna är lika långa")
        kvadratminne.append("Ja")
    else:
        print(f"Rektangeln har sidorna {s1} och  {s2}")
        kvadratminne.append("Nej")


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

    #Här kommer det jag behövede lägga till, hade redan lagrat in dom två sidorna i listor
    höjdenminne.append(volymantal)

    print('{:^10}'.format('Höjden  Volymen'))
    print('{:^10}'.format('---------------'))


    for i in range(1,volymantal):
        volymen = s1 * s2 * i
        print('{:2}'.format(i) + '{:>10}'.format(volymen))
    print('{:^10}'.format('---------------'))


while True:
    svar = str(input("Vill du utföra en beräkning Y/N: "))
    if svar == "Y":
        uppgift1() 
    else:
        clear()
        time.sleep(1)
        print("Beräkningar:")
        print(" ")
        for i in range(antalggr):
            print("--------------")
            print(f"Beräkning {i + 1}")
            print(f"Först sidan: {s1minne[i]} cm")
            print(f"Andra sidan: {s2minne[i]} cm")
            print(f"Arean: {areaminne[i]} cm3")
            print(f"Kvadrat: {kvadratminne[i]}")
            #La till en extra print bara för att tydligare visa att programmet fungerar
            print(f"Höjden jag räknat till: {höjdenminne[i]} cm")
            print("--------------")
            print(" ")
        break
