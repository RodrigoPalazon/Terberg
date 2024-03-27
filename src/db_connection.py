import sqlite3
from assets.vehicles_data import vehicles_data
from assets.website_data import website_data




# Create a connection to the database
conn = sqlite3.connect('../database/terberg.db')

# Create a cursor object
c = conn.cursor()

# Create table websites
c.execute("""CREATE TABLE IF NOT EXISTS websites
             (  website_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT, 
                url TEXT, 
                listing INTEGER)
          """)

# Create table vehicles
c.execute("""CREATE TABLE IF NOT EXISTS vehicles
             (  vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT, 
                subcategory TEXT, 
                price REAL)
          """)

# Create table vehicles_onwebsite table (N:N)
c.execute("""CREATE TABLE IF NOT EXISTS vehicles_on_website 
          ( website_id INTEGER,
            vehicle_id INTEGER,
            FOREIGN KEY (website_id) REFERENCES websites(website_id),
            FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
            PRIMARY KEY (ID));
          """)


# Clean vehicles_on_website before inserting data in it:
c.execute("DELETE FROM vehicles_on_website")

# Insert data into vehicles table
for item in vehicles_data:
    c.execute("INSERT INTO vehicles (name, subcategory, price) VALUES (?, ?, ?)", (item['name'], item['subcategory'], item['price']))
    vehicle_id = c.lastrowid  # Retrieve the auto-generated vehicle_id

# Insert data into website table
for item in website_data:
    c.execute("INSERT INTO websites (name, url, listing) VALUES (?, ?, ?)", (item['name'], item['url'], item['listing']))

# Insert data into vehicle_on_website table
c.execute("SELECT * FROM vehicles_on_website WHERE website_id = ? AND vehicle_id = ?", (1, 1))
if c.fetchone() is None:
    c.execute("INSERT INTO vehicles_on_website (website_id, vehicle_id) VALUES (?, ?)", (1, 1))

# and so on...


# Query to select all data from vehicles_on_website table
c.execute("SELECT * FROM vehicles_on_website")

# Fetch all rows from the query result
rows = c.fetchall()

# Iterate over the rows and print them
for row in rows:
    print(row)


# Commit changes and close connection
conn.commit()
conn.close()

