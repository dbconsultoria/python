#exemplo de unpivot
import pandas as pd
import io

# Import CSV

df = pd.read_csv(r"C:\Users\Rodrigo\Documents\GitHub\python\transpose.csv",header=0)
print(df)
df2=df.transpose()
print(df2)