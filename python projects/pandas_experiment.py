import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/lukeb/Desktop/python projects/name.basics.csv")
name = data["primaryName"]
born = data["birthYear"]
died = data["deathYear"]
print("name: "+name.head()+"  birthyear: "+born.head())
#name_born_died = data[["primaryName", "birthYear", "deathYear"]]
#print(name_born_died.head())

#after_2000 = data[data["primaryName"] > 1999]
#print(after_2000.head())

#birth_2005 = data[(data["birthYear"] == 1940)]
#print(birth_2005.head())
#data["birthYear"] > 35