#Kör i moment04-e.py

#Area uträknings funktionen, sparar arean i en lista.
def area(s1, s2):
    areaminne = s1 * s2
    return areaminne


#Omkrets uträknings funktionen, sparar omkretsen i en lista.
def omkrets(s1, s2):
    omkretsminne = 2*(s1+s2)
    return omkretsminne


#Kvadrat uträkningsfunktionen, sparar om det är en kvadrat eller inte i en lista.
def kvadrat(s1, s2):
    if s1 == s2:
        kvadratminne = "Ja"
    else:
        kvadratminne = "Nej"
    return kvadratminne


#Volym uträknings funktionen, sparar volymen från 1 -> höjden
def volym(s1, s2, höjd):
    volymminne = []
    for i in range(höjd):
        volymminne.append(s1 * s2 * (i+1))
    return volymminne

