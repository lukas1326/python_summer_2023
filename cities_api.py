from sqlalchemy import create_engine
from sqlalchemy import text
import pymysql
import requests as req
import pandas as pa

engine = create_engine("mysql+pymysql://root:@localhost/python2")

import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"



headers = {
	"X-RapidAPI-Key": "8a627d9886msh28af55539327f12p197e75jsn65eefaf3ee69",
	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
countries_data = response.json()['data']
countries = pa.json_normalize(countries_data)
countries.to_sql(name="cities",con=engine,index=False,if_exists="replace")
with engine.begin() as con:
    cities = pa.read_sql(text("SELECT * FROM cities"),con)
    
print(cities)








