import sqlite3
from assets.vehicles_data import vehicles_data
from assets.website_data import website_data


# Create a connection to the database
conn = sqlite3.connect('../database/terberg.db')

# Create a cursor object
c = conn.cursor()

# Create table vehicles
c.execute("""CREATE TABLE IF NOT EXISTS listings
             (  name TEXT, 
                subcategory TEXT, 
                price REAL)
          """)

# Create table websites
c.execute("""CREATE TABLE IF NOT EXISTS website
             (  name TEXT, 
                url TEXT, 
                listing INTEGER)
          """)

# Insert data into vehicles table
for item in vehicles_data:
    c.execute("INSERT INTO listings VALUES (?, ?, ?)", (item['name'], item['subcategory'], item['price']))

# Insert data into website table
for item in website_data:
    c.execute("INSERT INTO website VALUES (?, ?, ?)", (item['name'], item['url'], item['listing']))

# Insert data into vehicle_on_website table
    #  TO DO

# Commit changes and close connection
conn.commit()
conn.close()


