#pip install pyarrow
import pandas as pd
import pyarrow.parquet as pq

#o arquivo parquet deste script foi gerado com o código abaixo
df = pd.DataFrame({
    'student': ['personA007', 'personB', 'x', 'personD', 'personE'],
    'marks': [20,10,22,21,22],
})
df.to_parquet(R'C:\Users\Rodrigo\Documents\GitHub\python\sample.parquet')

#para "ler" o arquivo parquet (na verdade, transformá-lo em um dataframe)
df = pd.read_parquet(R'C:\Users\Rodrigo\Documents\GitHub\python\sample.parquet')
print(df)