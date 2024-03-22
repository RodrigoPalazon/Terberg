from src.assets.vehicles_on_website import vehicles_on_website
from src.assets.website_data import website_data
from src.assets.vehicles_data import vehicles_data
from src.assets.banner import *
from src.view.story_functions import *
import src.model.crud_functions
from tabulate import tabulate

def main():
    print('\n' * 2)
    print_banner()
    print('\n' * 2)
    while True:
        view_manage = view_or_manage_data()
        
        if view_manage == "1":
                
            while True:
                choice = input("""Which table would you like to check data from ?

                \t1. Websites Table, individually.
                \t2. Vehicles Table, individually.
                \t3. Full Data Table.
                \t4. Quit the application

Type the number of your choice: """)
                
                if choice == "1":
                    print('\n' * 2)
                    website_data_truncated = [{**entry, "url": truncate_url(entry["url"])} for entry in website_data]
                    print(tabulate(website_data_truncated, headers='keys', tablefmt="grid"))
                    print('\n' * 2)
                elif choice == "2":
                    print('\n' * 2)
                    vehicles_data_with_rowid = [{"rowid": i+1, **vehicle} for i, vehicle in enumerate(vehicles_data)]
                    print(tabulate(vehicles_data_with_rowid, headers="keys", tablefmt="grid"))
                    print('\n' * 2)
                elif choice == "3":
                    print('\n' * 2)
                    print('\t We apologise, this functionality is still working in progress.')
                    print('\n' * 2)
                elif choice == "4":
                    print('\n' * 2)
                    print("\t Thank you for using the application. Goodbye!")
                    print('\n' * 2)
                    break  
                else:
                    print('\n' * 2)
                    print("Invalid choice. Please select a valid option.")
                    print('\n' * 2)
        
        elif view_manage == "2":
            print("Working in progress !")
        break
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