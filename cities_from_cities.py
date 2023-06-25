from sqlalchemy import create_engine
import requests 
from sqlalchemy import text
import pandas as pd
import time

engine = create_engine("mysql+pymysql://root:@localhost/python2")

with engine.begin() as con:
    cities = pd.read_sql(text("SELECT * FROM cities"),con)
    
# print(cities)

# print(cities.to_json())
a = cities.wikiDataId.values

def kmFromCity (wikiDataId):

    near_city_list=[]
    for id in wikiDataId:
        
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/"+id+"/nearbyCities"

        querystring = {"radius":"100"}

        headers = {
            "X-RapidAPI-Key": "8a627d9886msh28af55539327f12p197e75jsn65eefaf3ee69",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        time.sleep(10)
        b=response.json()["data"]
        for item in b:
            item['fromCity'] =id
        near_city_list = b+near_city_list
    return near_city_list
    

nearcities_data = kmFromCity(a)
print(nearcities_data)

nearcities = pd.json_normalize(nearcities_data)
nearcities.to_sql(name="nearcities",con=engine,index=False,if_exists="replace")  

