"""
@author Luis Calderon

"""

import pandas as pd

datos = pd.read_csv('Sample test file - Sheet1.csv',header = 0)
#datos = datos.dropna(how='all')
print(datos)

## Nombres ordenados alfabeticamente ## 
datos_nombres_ordenados = datos.sort_values(by='First Name')
datos_nombres_ordenados = datos_nombres_ordenados[['First Name','Last Name']]

## Funcion

def normalize(s):
    replacements = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def isNaN(num):
    return num != num



for j in range(len(datos)):
    if isNaN(datos['First Name'][j]):
        raise TypeError("El nombre está vacío.")
    else:          
        datos['First Name'][j]=normalize(datos['First Name'][j])  
        print(datos['First Name'][j])