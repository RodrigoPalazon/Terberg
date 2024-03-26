# from src.assets.vehicles_on_website import vehicles_on_website
from src.assets.website_data import website_data
from src.assets.vehicles_data import vehicles_data
from src.assets.banner import *
from src.view.story_functions import *
# import src.model.crud_functions
from tabulate import tabulate

def main():
    print('\n' * 2)
    print_banner()
    print('\n' * 2)
    while True:
        view_manage = question_view_or_manage_data()
        
        if view_manage == "1":        
            while True:
                choice = question_witch_table_display() 
                if choice == "1":
                    display_website_table(website_data)
                elif choice == "2":
                    display_vehicles_table(vehicles_data)
                elif choice == "3":
                    display_full_data_table()
                elif choice == "4":
                    display_quit_message()
                    break
                else:
                    print('\n' * 2)
                    print("Invalid choice. Please select a valid option.")
                    print('\n' * 2)
            break   
        elif view_manage == "2":
            print("Working in progress !\n")
        
if __name__ == "__main__":
    main()


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




# Testing git clone