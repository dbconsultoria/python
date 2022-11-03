import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'A Api está no ar'

@app.route('/myjson')
def myjson():
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
  return data

app.run(host='0.0.0.0')
