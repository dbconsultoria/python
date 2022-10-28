import pandas as pd

data = pd.read_csv (r'C:\Users\Rodrigo\Documents\GitHub\python\products.csv',header=0)   
df = pd.DataFrame(data)
print(df)
df.fillna('0',inplace=True)
print(df)