from tabulate import tabulate
from src.assets.website_data import website_data
from src.assets.banner import *


def print_banner():

    for line in banner:
        print(line)
    message = "WELCOME TO TERBERG BUSINESS CASE"    
    width=50
    # Calculate the padding for the message
    padding = (width - len(message) - 2) // 2
    # Top border
    print("+" + "-" * (width - 2) + "+")
    # Padding and message row
    print("|" + " " * padding + message + " " * padding + (" " if len(message) % 2 == 0 else "") + "|")
    # Bottom border
    print("+" + "-" * (width - 2) + "+")
    # Example of printing the banner

def question_view_or_manage_data():
    view_or_manage = input("""A) What would you like to do ?

            \t1. View Data.
            \t2. Manage Data.

    Type the number of your choice: """)
    return view_or_manage

def question_witch_table_display():
    choice = input("""Which table would you like to check data from ?

                \t1. Websites Table, individually.
                \t2. Vehicles Table, individually.
                \t3. Full Data Table.
                \t4. Quit the application

Type the number of your choice: """)
    return choice

def truncate_url(url, max_length=30):
    return (url[:max_length] + '...') if len(url) > max_length else url

def display_website_table(website_data):
    website_data_truncated = [{**entry, "url": truncate_url(entry["url"])} for entry in website_data]
    print('\n' * 2)
    print(tabulate(website_data_truncated, headers='keys', tablefmt="grid"))
    print('\n' * 2)

def display_vehicles_table(vehicles_data):
    vehicles_data_with_rowid = [{"rowid": i+1, **vehicle} for i, vehicle in enumerate(vehicles_data)]
    print('\n' * 2)
    print(tabulate(vehicles_data_with_rowid, headers="keys", tablefmt="grid"))
    print('\n' * 2)

def display_full_data_table():
    print('\n' * 2)
    print('\t We apologise, this functionality is still work in progress.')
    print('\n' * 2)

def display_quit_message():
    print('\n' * 2)
    print("\t Thank you for using the application. Goodbye!")
    print('\n' * 2)

# while True:
#     choice = input("""Which table would you like to check data from ?
                    
#                     \t1. Websites Table, individually.
#                     \t2. Vehicles Table, individually.
#                     \t3. Full Data Table.
#                     \t4. Quit the application

#     Type the number of your choice: """)
    
#     if choice == "1":
#         display_website_table(website_data)
#     elif choice == "2":
#         display_vehicles_table(vehicles_data)
#     elif choice == "3":
#         display_full_data_table()
#     elif choice == "4":
#         display_quit_message()
#         break
#     else:
#         print('\n' * 2)
#         print("Invalid choice. Please select a valid option.")
#         print('\n' * 2)
