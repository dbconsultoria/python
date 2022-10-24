#pip install beautifulsoup4
#pip install lxml
#fonte: https://medium.com/analytics-vidhya/web-scraping-a-wikipedia-table-into-a-dataframe-c52617e1f451
#data: 24/10/2022
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

# pegar response em html
wikiurl="https://en.wikipedia.org/wiki/List_of_cities_in_Brazil_by_population"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)

# parse dos dados usando o bsoup
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})
# aqui atribui a tabela com os dados em uma var
df=pd.read_html(str(indiatable))
# convert a lista em datafram
df=pd.DataFrame(df[0])
print(df.head())

# retirar colunas indesejadas
data = df.drop(["2021 Estimate"], axis=1)
# renomear colunas
data = data.rename(columns={"2010 Census": "Population 2010"})
# mostra os resultados
print(data)

