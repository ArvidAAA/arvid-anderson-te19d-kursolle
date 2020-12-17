#Created 2020-10-22
#Inlämmingsuppgift moment04

#Måste ha plotly installerat.
import plotly.graph_objects as go
import numpy
import pandas as pd


def uppgift1():
    
    ########################################
    print("Inlämmningsuppgift moment04 a")
    ########################################
    #Skapat dessa för att inte Visual Studio Code ska jobba sig
    s1 = 0
    s2 = 0
    #Input för heltal 1 och 2
    s1 = int(input("Ange ena sidan på rektangeln: "))
    s2 = int(input("Ange andra sidan på rektangeln: "))
    

    #Area = b * h
    area = s1 * s2
    #Printar ut arean
    print(f"Arean på rektangeln är {area}")

    if s1 == s2:
        print(f"Rektangeln har sidorna {s1} och {s2} detta betyder att det är en kvadrat eftersom sidorna är lika långa")
    else:
        print(f"Rektangeln har sidorna {s1} och  {s2}")

    #Plotly för graf
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Höjden', 'Volymen'],
                    line_color='darkslategray',
                    fill_color='lightskyblue',
                    align='left'),
        cells=dict(values=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        [1 * s1 * s2, 2 * s1 * s2, 3 * s1 * s2, 4 * s1 * s2, 5 * s1 * s2, 6 * s1 * s2, 7 *s1 *s2, 8 * s1 * s2, 9 * s1 * s2, 10 * s1 * s2]], # 2nd column
                line_color='darkslategray',
                fill_color='lightcyan',
                align='left'))
    ])

    fig.update_layout(width=500, height=900)
    fig.show()
    
uppgift1()


