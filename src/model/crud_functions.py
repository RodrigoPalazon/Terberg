import sqlite3
import os
# from src.db_connection import *

def add_one(name, subcategory, price):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    c.execute("INSERT INTO listings VALUES (?,?,?)", (name, subcategory, price))
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    c.executemany("INSERT INTO listings VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

def delete_one(table, id):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    c.execute("DELETE FROM {} WHERE rowid={}".format(table,id))
    conn.commit()
    conn.close()

def email_lookup(email):
    conn = sqlite3.connect('terber.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM listings WHERE email={}".format(email))
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

def print_table(table):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    # Query the Database
    c.execute("SELECT rowid,* FROM {}".format(table))
    items =c.fetchall()
    # print(items)

    for item in items:
        # print(str(item[0]) + " " + item[1] + "| \t" + item[2] + " " + str(item[3]))
        print(item)
    # print(c.fetchone()[0])

    # Commit changes and close connection
    conn.commit()
    conn.close()

def display_joinned_table():
    # conn = sqlite3.connect('C:/Users/RodrigoRiquenaPalazo/Documents/Rockfeather/Traineeship/Terberg_correct_repo/Terberg/database/terberg.db')
    # Get the directory of the current script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to the database file
    db_path = os.path.join(script_dir, '..', '..', 'database', 'terberg.db')

    # Connect to the database using the relative path
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
        # Display joinned tables Vehicles and Websites as one.
    c.execute("""
        SELECT vehicles.*, websites.*
        FROM vehicles
        JOIN vehicles_on_website ON vehicles.vehicle_id = vehicles_on_website.vehicle_id
        JOIN websites ON websites.website_id = vehicles_on_website.website_id
    """)

    # Fetch and display the results from the joinned table
    display_joinned_table = c.fetchall()
    for row in display_joinned_table:
        print(row)  # Modify this to display the data as desired
        
    conn.close()
    