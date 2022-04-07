"""
@author Luis Calderon

"""

import pandas as pd
datos = pd.read_csv('Sample test file - Sheet1.csv',header = 0)
print(datos)
print(datos['First Name'])