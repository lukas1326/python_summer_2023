from functools import reduce
from collections import defaultdict

with open("r_text.txt","r") as f:
    text = 

def map_function(line):
    words = line.split()
    words_countt = defaultdict(int)
    for word in words:
        words_countt[word]+=1
    return words_countt.items()

def reduce_function(word,counts):
    return word,sum(counts)
