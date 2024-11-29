import kagglehub
import pandas as pd
import requests
from mysql import connector
import pyodbc
import json

# Step 1: Read Data

# hent data fra
# SQL proev pyodbc
# et API
# et kaggle dataset

path = kagglehub.dataset_download("valakhorasani/gym-members-exercise-dataset")


print("Path to dataset files:", path)

# SQL (northwind f eks)
connection = connector.connect(user='root', password= 'Deter1dagSpecialisterne', host='localhost', database = 'northwind')
cursor = connection.cursor() # alle tabeller
cursor.execute("SELECT * FROM products ORDER BY UnitPrice;")
res = cursor.fetchall()
results = cursor.stored_results()
print(results)
print(res)
print('end')

#API... aendr gerne til en tabel som er relevant for de andre tabeller
#eks fra # https://www.dataquest.io/blog/python-api-tutorial/
response = requests.get("http://api.open-notify.org/astros")
print("API:")
print(response.status_code)
print("API done")
print(response.content) #json

data = json.loads(response.content) # json til dictionary

persons = data['people']

for person in persons:
    person_object = Person(person) # f eks def klasse
print()


# Step 2: Transform data
    # for each data source (SQL, API, CSV)
    # make a table and transform the data

# Step 3: Save data to SQL
    # for each data frame
    #   write to SQL