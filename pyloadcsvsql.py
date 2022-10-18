#setx PATH "%PATH%;D:\Users\Rodrigo\AppData\Local\Programs\Python\Python310\Scripts"
#pip install pandas
#pip install pyodbc
import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv (r'C:\Users\Rodrigo\Documents\GitHub\python\products.csv',header=0)   
df = pd.DataFrame(data)

#print(df)

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LUS1EE3;'
                      'Database=dba;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE tbxproducts (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():

    cursor.execute('''
                INSERT INTO tbxproducts (product_id, product_name, price)
                VALUES (?,?,?)
                ''',
                row.product_id, 
                row.product_name,
                row.price
                )

conn.commit()