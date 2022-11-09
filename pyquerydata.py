#pip install pandas
import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv (r'C:\Users\Rodrigo\Documents\GitHub\python\products.csv',header=0)   
print(data)

#query one condition
data.query('price > 200', inplace=True)
print(data)

data.query('price > 200' and 'product_id < 5', inplace=True)
print(data)