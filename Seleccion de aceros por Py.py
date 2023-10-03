 import pandas as pd
direccion = r'C:\Users\usuario\Documents\Joaquin\Base datos aceros.xlsx'
pd.read_excel(direccion, sheet_name= 'GENERAL')
datos_df = pd.read_excel(direccion, sheet_name= 'GENERAL')

condicion = datos_df.loc [:,"denominacion"]
print (condicion)

dato= int(input("Seleccione un acero por el indice de la izquierda:"))

condicion2 = datos_df.loc [dato,:]

print(condicion2)
