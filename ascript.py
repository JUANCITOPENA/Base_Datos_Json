import pandas as pd
import json

# Lee el archivo de Excel
df = pd.read_excel('datos_ventas_Version_Final_Muestra_20242000.xlsx', engine='openpyxl')

# Convierte las columnas Timestamp a cadenas de texto
df['fecha_factura'] = df['fecha_factura'].astype(str)

# Convierte el DataFrame de pandas a un diccionario
data_dict = df.to_dict(orient='records')

# Convierte el diccionario a formato JSON
json_data = json.dumps(data_dict, indent=4)

# Guarda el JSON en un archivo
with open('datos.json', 'w') as json_file:
    json_file.write(json_data)

print('El archivo JSON ha sido creado correctamente.')
