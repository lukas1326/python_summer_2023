from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
from collections import namedtuple

engine = create_engine("mysql+pymysql://root:@localhost/python2")

with engine.begin() as con:
    cities = pd.read_sql(text("SELECT * FROM cities"),con)
    nearcities = pd.read_sql(text("SELECT * FROM nearcities"),con)
    

# 1)Use map to double each element in a list of numbers.
# Use filter to select only the odd numbers from a list of integers.
# Pandas:

def double (x):
    return x*2

distance = nearcities.distance.values

double_distance = list(map(double,distance))
filtered_distance = list(filter(lambda x: (x*100 % 2 != 0), distance))

# 2)Read a CSV file into a pandas DataFrame and display the first few rows.
# Group a DataFrame by a specific column and calculate the average of another column.
# Merge two DataFrames based on a common column.

# print (nearcities.groupby('fromCity')["distance"].mean())
# print (nearcities.merge(cities,how='left',left_on='fromCity',right_on='wikiDataId'))

# Namedtuple:


cities_tuple = namedtuple('city',['name','country','population'])
tuple_list = list(cities[['name','country','population']].itertuples(index=False,name='cities_tuple'))
print(tuple_list)
for item in tuple_list:
    print(item.name)
    print(item[1])
    print(getattr(item,'name'))


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