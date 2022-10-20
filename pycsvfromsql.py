#dia: 20/10/2022
#pip install sqlalchemy
import pandas as pd
import pyodbc 
import sqlalchemy

from sqlalchemy.engine import URL
connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-LUS1EE3;DATABASE=dba;UID=sa;PWD=sa"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

from sqlalchemy import create_engine
engine = create_engine(connection_url)

sql_query = pd.read_sql_query(''' 
                              select * from dba.dbo.tbxproducts
                              '''
                              ,engine) # 'conn' eh a var que contem a conexao com o banco

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\Rodrigo\Documents\GitHub\python\exported_data.csv', index = False) # o 'r' no começo do path eh necessario