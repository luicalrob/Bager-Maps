"""
@author Luis Calderon

"""

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


## Lectura de datos 
datos = pd.read_csv('Sample test file - Sheet1.csv',header = 0)
#datos = datos.dropna(how='all')
#print(datos)



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
datos_fechas_ordenados_df = pd.DataFrame({'Last Check-In Date': pd.to_datetime(datos_fechas_ordenados)})
print("\n")
print(datos_fechas_ordenados_df)
print("\n")

cliente_antiguo=""
cliente_reciente=""
j=0     # variables auxiliar para encontrar la fecha mas reciente y la mas antigua



# guardo el nombre mas antiguo y el mas reciente

for index, row in datos_fechas_ordenados_df.iterrows():
    if j==0:    # mas antiguo    
        cliente_antiguo=datos['First Name'][index]
        cliente_antiguo+=" "
        cliente_antiguo+=datos['Last Name'][index]
        num_antiguo=index
    if j==len(datos)-1-i:
        cliente_reciente=datos['First Name'][index]
        cliente_reciente+=" "
        cliente_reciente+=datos['Last Name'][index]
        num_reciente=index
    j+=1

print("\nEl customer con el check-in date más antiguo es", cliente_antiguo,".")
print("\nEl customer con el check-in date más antiguo es", cliente_reciente,".")




# dar required files de los clientes obtenidos

# cada uno en un dataframe separado
datos_cliente_antiguo_df = pd.DataFrame({'Name':cliente_antiguo, 'Street':(datos['Street'][num_antiguo]), 'Zip':(datos['Zip'][num_antiguo]), 'City':(datos['City'][num_antiguo]), 'Last Check-In Date':(datos['Last Check-In Date'][num_antiguo]), 'Company':(datos['Company'][num_antiguo])},index=[0])
datos_cliente_reciente_df = pd.DataFrame({'Name':cliente_reciente, 'Street':(datos['Street'][num_reciente]), 'Zip':(datos['Zip'][num_reciente]), 'City':(datos['City'][num_reciente]), 'Last Check-In Date':(datos['Last Check-In Date'][num_reciente]), 'Company':(datos['Company'][num_reciente])},index=[0])

# los dos en un dataframe unido
#datos_clientes_df = pd.DataFrame({'Name':cliente_antiguo, 'Street':(datos['Street'][num_antiguo]), 'Zip':(datos['Zip'][num_antiguo]), 'City':(datos['City'][num_antiguo]), 'Last Check-In Date':(datos['Last Check-In Date'][num_antiguo]), 'Company':(datos['Company'][num_antiguo])},index=[0])
#datos_clientes_df = pd.DataFrame({'Name':[cliente_antiguo,cliente_reciente], 'Street':(datos['Street'][num_reciente]), 'Zip':(datos['Zip'][num_reciente]), 'City':(datos['City'][num_reciente]), 'Last Check-In Date':(datos['Last Check-In Date'][num_reciente]), 'Company':(datos['Company'][num_reciente])},index=[1])
datos_clientes_df = pd.DataFrame({'Name':[cliente_antiguo,cliente_reciente] ,'Street':[datos['Street'][num_antiguo],datos['Street'][num_reciente]] , 'Zip':[(datos['Zip'][num_antiguo]), (datos['Zip'][num_reciente])] , 'City':[(datos['City'][num_antiguo]), (datos['City'][num_reciente])], 'Last Check-In Date':[(datos['Last Check-In Date'][num_antiguo]), (datos['Last Check-In Date'][num_reciente])], 'Company':[(datos['Company'][num_antiguo]), (datos['Company'][num_reciente])]}, index=[0, 1])

# comprobar datos de cada cliente

for index, row in datos_clientes_df.iterrows():
    if isNaN(row['Street']):
        if index==0:
            print("\nError: La dirección del cliente más antiguo está vacía.")
        else:
            print("\nError: La dirección del cliente más reciente está vacía.")
    if isNaN(row['Zip']):
        if index==0:
            print("\nError: El Zip del cliente más antiguo está vacío.")
        else:
            print("\nError: El Zip del cliente más reciente está vacío.")
    if isNaN(row['City']):
        if index==0:
            print("\nError: La ciudad del cliente más antiguo está vacía.")
        else:
            print("\nError: La ciudad del cliente más reciente está vacía.")
    if isNaN(row['Last Check-In Date']):
        if index==0:
            print("\nError: El último Check-in date del cliente más antiguo está vacío.")
        else:
            print("\nError: El último Check-in date del cliente más reciente está vacío.")
    if isNaN(row['Company']):
        if index==0:
            print("\nError: La compañia del cliente más antiguo está vacía.")
        else:
            print("\nError: La compañia del cliente más reciente está vacía.")
  

print("\n")
print(datos_clientes_df)
