from src.assets.website_data import website_data
from src.assets.vehicles_data import vehicles_data
from src.assets.banner import *
import src.model.crud_functions
from tabulate import tabulate


def truncate_url(url, max_length=30):
    return (url[:max_length] + '...') if len(url) > max_length else url

def print_banner(message, width=50):
    # Calculate the padding for the message
    padding = (width - len(message) - 2) // 2
    # Top border
    print("+" + "-" * (width - 2) + "+")
    # Padding and message row
    print("|" + " " * padding + message + " " * padding + (" " if len(message) % 2 == 0 else "") + "|")
    # Bottom border
    print("+" + "-" * (width - 2) + "+")

message = "WELCOME TO TERBERG BUSINESS CASE"

# Example of printing the banner
for line in banner:
    print(line)

def main():
    print()
    print()
    print_banner(message)
    print()
    print()
    while True:
        print("Which table would you like to check the data in ?")
        print()
        print("\t1. website_data")
        print("\t2. vehicles_data")
        print("\t3. Quit the application")
        print()
        choice = input("Type the number of your choice: ")
        
        if choice == "1":
            print()
            website_data_truncated = [{**entry, "url": truncate_url(entry["url"])} for entry in website_data]
            print(tabulate(website_data_truncated, headers='keys', tablefmt="grid"))
            print()
        elif choice == "2":
            print()
            vehicles_data_with_rowid = [{"rowid": i+1, **vehicle} for i, vehicle in enumerate(vehicles_data)]
            print(tabulate(vehicles_data_with_rowid, headers="keys", tablefmt="grid"))
            print()
        elif choice == "3":
            print()
            print("Thank you for using the application. Goodbye!")
            print()
            print()
            break
        else:
            print()
            print("Invalid choice. Please select a valid option.")
            print()

if __name__ == "__main__":
    main()

# def main():
    # Ask for user name
    # username = input("Please pick a user name: ")
    
    # Password setup with confirmation
    # while True:
    #     password = input("Please enter your password: ")
    #     password_confirm = input("Please confirm your password: ")
    #     if password == password_confirm:
    #         break
    #     else:
    #         print("Passwords do not match. Please try again.")
    
    # Main loop for user actions
    # while True:
    #     print("\nWhat would you like to do?")
    #     print("1. Option 1")
    #     print("2. Option 2")
    #     print("3. Option 3")
    #     print("4. Quit the application")
        
        # User picks an option
        # choice = input("Please enter the number of your choice: ")
        
        

# if __name__ == "__main__":
#     main()



# print("#########   TERBERG  BUSINESS CASE ##########")
# functions.add_one("Ferrari","Sport",420000)
# functions.print_table("listings")

# newTrucks = [
#     ("Master Truck","Extra Power", 6666),
#     ("Tiny Monster","Compact", 200)
# ]

# print("***************************************")
# functions.add_many(newTrucks)


# functions.print_table("website")




