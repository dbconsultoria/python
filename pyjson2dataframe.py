import pandas as pd
import json
from pandas import json_normalize

data = '''
{
"technologies":
         [
         { "Courses": "Spark", "Fee": 22000,"Duration":"40Days"},
         { "Courses": "PySpark","Fee": 25000,"Duration":"60Days"},
         { "Courses": "Hadoop", "Fee": 23000,"Duration":"50Days"}
         ]
}
'''

#lendo como records
df = pd.read_json(data,orient="records")
print(df)

# Create JSON data with student details
data = '''
{
    "student-1": { "id": "1", "name": "sravan","age":22 },
    "student-2":{ "id": "2", "name": "harsha","age":22 },
    "student-3": { "id": "3", "name": "deepika","age":21 },
    "student-4": { "id": "4", "name": "jyothika","age":23 }
} '''

# lendo como index
df = pd.read_json(data,orient ='index')
print(df)