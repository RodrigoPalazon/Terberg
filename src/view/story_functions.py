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

def view_or_manage_data():
    view_or_manage = input("""A) What would you like to do ?

            \t1. View Data.
            \t2. Manage Data.

    Type the number of your choice: """)
    return view_or_manage

def truncate_url(url, max_length=30):
    return (url[:max_length] + '...') if len(url) > max_length else url