"""

moment04-d
Arvid Anderson TE19D

Uppgift a, b, c, d har bara en funktion denna gången jag gör flera olika funktioner, har valt att lägga berkäningsfunktionerna så som area, omkrets, kvadrat och volym i calc.py och sedan importera i denna
python filen. Så sätt blir det lite mer strukturerat och jag slipper ha så mycket i detta dokument. 

Jag är väl medveten om att man hade kunnat spara allt i en lista med flera listor i dock är detta mer tydligt i koden. Tycker att använda funktioner var mycket bättre en det jag gjorde innan.




Area, omkrets, kvadrat, höjden, volym
"""


#Har lagt in alla uträknings funktioner i calc.py därför import calc, samt gjort en global counter för antalet ggr jag kör min if sats i while truen
import subprocess
import platform
import time
import calc
global antal_loop
antal_loop = 0
#Clear function
def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)

#Skapar listor för att spara informationen varje gång jag utfört en beräkning
s1minne = []
s2minne = []
areaminne = []
omkretsminne = []
kvadratminne = []
volymminne = []
hojdenminne = []


#While True, game loop
while True:
    användare_input = str(input("Vill du utföra en beräkning Y/N: "))
    if användare_input == "Y" or användare_input == "y":
        antal_loop += 1
        s1 = int(input("Mata in s1: "))
        s2 = int(input("Mata in s2: "))

        while True:
            try:
                höjd = int(input("Mata in höjd: "))
                break
            except:
                print("Det är inget heltal! Försök igen")
        
        if höjd < 0:
            höjd = 1+1
        else:
            pass
        if höjd > 10:
            höjd = 10+1
        else:
            pass

        s1minne.append(s1)
        s2minne.append(s2)
        areaminne.append(calc.area(s1, s2))
        omkretsminne.append(calc.omkrets(s1, s2))
        kvadratminne.append(calc.kvadrat(s1, s2))
        volymminne.append(calc.volym(s1, s2, höjd))
        hojdenminne.append(höjd)

    else:
        clear()
        time.sleep(1)
        print("Beräkningar:")
        print(" ")
        for i in range(antal_loop):
            print("--------------")
            print(f"Beräkning {i + 1}")
            print(f"Först sidan: {s1minne[i]} cm")
            print(f"Andra sidan: {s2minne[i]} cm")
            print(f"Arean: {areaminne[i]} cm2")
            print(f"Omkrets: {omkretsminne[i]} cm")
            print(f"Kvadrat: {kvadratminne[i]}")
            print(f"Volymen 1-{hojdenminne[i]}: {volymminne[i]} (cm3)")
            print("--------------")
            print(" ")
        break