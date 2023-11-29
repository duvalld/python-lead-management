from json import load, dump
from tabulate import tabulate
from time import sleep

 
# JSON File Path
json_file_path = "python-lead-management/lms.json"
 
# Open json file in read-only mode
with open(json_file_path, 'r') as file:
    # print json load result in table form using tabulate method
    print(tabulate(load(file), headers="keys", tablefmt="pretty"))
 
# search function asking for json load result, dictionary key and search keyword
def search(data, dict_key, keyword):
    list_dict = []
    count_results = 0
    for item in data:
        # check if item contains keyword
        if keyword.lower() in item[dict_key].lower():
            list_dict.append(item)
            count_results += 1
    # print search result in table form
    print(tabulate(list_dict, headers="keys", tablefmt="pretty"))
    # print count of result items
    print(f"Results: {count_results}")

use = True
while use:
    # re-open json file with read only mode
    with open(json_file_path, 'r') as file:
        data = load(file)
    # LMS menu (Viewing, Adding or Exit)
    menu_input = input("Enter 1 for View, 2 for adding new item, 3 to exit program: ")
    # Option 1: Viewing Items
    if menu_input == "1":
        view_menu_input = input("Enter 1 to search via Name, 2 to search via Contact number, 3 to search via Email Address: ")
        # Search via Name
        if view_menu_input == "1":
            search_input = input("Search Name:")
            search(data, "name", search_input)
        # search via contact_number
        elif view_menu_input == "2":
            search_input = input("Search Contact Number:")
            search(data, "contact_number", search_input)
        # search via email
        elif view_menu_input == "3":
            search_input = input("Search Email Address:")
            search(data, "email", search_input)
    # Option 2: Adding Item
    elif menu_input == "2":
        print("Add New Item")
        name_input = input("Name:")
        contact_input = input("Contact Number:")
        email_input = input("Email Address:")
        # append data list with the name_input, contact_input, email_input value
        data.append({"name":name_input,"contact_number":contact_input,"email":email_input})
       
        adding = True
        while adding:
            # ask user if they wants to proceed in saving the record
            confirmation = input("do you want save the record ? y/n:")
            if confirmation.lower() == "y":
                # open file with write mode and ensure that the file is closed after excuted
                with open(json_file_path, 'w') as file:
                    # write file with data from appended list variable
                    dump(data,file)
                # open json file with read only mode
                with open(json_file_path, 'r') as file:
                    # assign json result to a variable
                    new_data = load(file)
                # print result in table form
                print(tabulate(new_data, headers="keys", tablefmt="pretty"))
                # change adding variable to False to stop the loop
                adding = False
            elif confirmation.lower() == "n":
                # remove recently added item to data list
                data.pop()
            else:
                # invalid entry message
                print("Invalid Entry: Enter y if YES or n for NO")
    elif menu_input == "3":
        print("Exiting...")
        sleep(2)
        # change use variable value to False to stop the loop and exit the program
        use = False
    else:
        print("Invalid Entry, Enter 1, 2 or 3 only!")