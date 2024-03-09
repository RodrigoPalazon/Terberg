import sqlite3
import sys
import os

# Calculate the absolute path to the directory containing 'cleaned_data.py'
data_dir = os.path.abspath("C:/Users/RodrigoRiquenaPalazo/Documents/Rockfeather/Traineeship/Terberg_correct_repo/data/resources")

# Add this directory to sys.path
sys.path.append(data_dir)

# Now you can import the 'data' variable from 'cleaned_data.py'
from vehicles_data import data

# The rest of your script where you use 'data'

# Create a connection to the database
conn = sqlite3.connect('../data/db/terberg.db')

# Create a cursor object
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS listings
             (  name TEXT, 
                subcategory TEXT, 
                price REAL)
          """)

# Insert data into table
for item in data:
    c.execute("INSERT INTO listings VALUES (?, ?, ?)", (item['name'], item['subcategory'], item['price']))

# # Query the Database
# c.execute("SELECT rowid,* FROM listings")
# items =c.fetchall()   
# # print(items)

# for item in items:
#     print(str(item[0]) + " " + item[1] + "| \t" + item[2] + " " + str(item[3]))
# # print(c.fetchone()[0])

# # Commit changes and close connection
conn.commit()
conn.close()


