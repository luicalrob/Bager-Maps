"""
@author Luis Calderon

"""

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


## Lectura de datos 
datos = pd.read_csv('Sample test file - Sheet1.csv',header = 0)
#datos = datos.dropna(how='all')
print(datos)



## Nombres ordenados alfabeticamente (ordenando los nombres, no los apellidos) 


datos_nombres_df = datos[['First Name','Last Name']]
datos_nombres_string = datos_nombres_df.astype({'First Name':'string','Last Name':'string'})  # Convertir a String

datos_fechas_df = datos[['Last Check-In Date']]
datos_fechas_date = pd.to_datetime(datos_fechas_df['Last Check-In Date'])




## Funciones

def normalize(s):   # función elimina tildes
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

def isNaN(num):     # funcion comprueba NaN
    return num != num



## obtencion de resultados

# obtenemos los full names
# for para detectar los vacios y para quitar las tildes de los nombres

for j in range(len(datos)):
    if isNaN(datos_nombres_df['First Name'][j]):
        print("\nError: El nombre está vacío en la posicion ", j,".")       
    else:
        datos_nombres_df['First Name'][j]=normalize(datos_nombres_df['First Name'][j])
        
# ordenamos los nombres
datos_nombres_ordenados = datos_nombres_df.sort_values(by='First Name')

salida = ["" for x in range(len(datos))]    # variable de salida de Full Names
i=0        # variable auxiliar para guardar donde hay nombres vacios

# introduzco en la salida los nombres ordenados
for index, row in datos_nombres_ordenados.iterrows():
    salida[i] = datos_nombres_string['First Name'][index]
    salida[i] += " "
    salida[i] += datos_nombres_string['Last Name'][index]
    i+=1
print("\n")
print(salida)


# obtenemos los clientes por fechas
# for para detectar los vacios
i=0     # variables auxiliar para saber cuantas fechas erroneas hay
for j in range(len(datos)):
    if isNaN(datos_fechas_df['Last Check-In Date'][j]):
        print("\nError: La fecha está vacía en la posición ", j,".")
        i+=1
       
# ordenamos las fechas
datos_fechas_ordenados = datos_fechas_date.sort_values()
print("\n")
print(datos_fechas_ordenados)

