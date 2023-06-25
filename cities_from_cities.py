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

# 1)Use map to double each element in a list of numbers.
# Use filter to select only the odd numbers from a list of integers.
# Pandas:



# 2)Read a CSV file into a pandas DataFrame and display the first few rows.
# Group a DataFrame by a specific column and calculate the average of another column.
# Merge two DataFrames based on a common column.
# Namedtuple:



# 3)Define a Person named tuple with fields for name, age, and city. Create instances of Person and access their attributes.
# Counter:

# 4)Count the frequency of each word in a given text and display the top 5 most common words.
# Merge two counters together and calculate the total count of each element.
# Deque:

# 5)Use a deque to implement a queue and perform enqueue and dequeue operations.
# Reverse the order of elements in a deque.
# Defaultdict:

# 6)Create a defaultdict that maps a character to a list of words starting with that character.
# Calculate the sum of values for each key in a dictionary using a defaultdict.
# Reduce:

# 7)Use reduce to find the maximum element in a list of numbers.
# Combine a list of strings into a single string using reduce.