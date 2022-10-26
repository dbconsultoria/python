#setx PATH "%PATH%;D:\Users\Rodrigo\AppData\Local\Programs\Python\Python310\Scripts"
#pip install pandas
#pip install pyodbc
#pip install numpy
import pandas as pd
import numpy as np
import math

# Importar CSV
data = pd.read_csv (r'C:\Users\Rodrigo\Documents\GitHub\python\products.csv',header=0)   
df = pd.DataFrame(data)
print(df)

# loop dataframe
for row in df.itertuples():
    #se o valor for NaN colocar zero no df
    if math.isnan(row.price):
        print('Valor nulo encontrado')
        df.at[row.Index,'price']=0
    
print(df)