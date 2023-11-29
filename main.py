import json

json_file_path = "python-lead-management/lms.json"

with open(json_file_path, 'r') as file:
    data = json.load(file)

for item in data:
    for key, value in item.items():
        print(f"{key} : {value}")

use = True
while use:
    menu_input = input("Enter 1 for View, 2 for adding new item, 3 to exit program: ")
    if menu_input == "1":
        view_menu_input = input("Enter 1 to search via Name, 2 to search via Contact number, 3 to search via Email Address: ")
        if view_menu_input == "1":
            search_input = input("Search Name:")
            for item in data:
                result = []
                if item["name"] == search_input:
                    print(item)
        elif view_menu_input == "2":
            search_input = input("Search Contact Number:")
            for item in data:
                result = []
                if item["contact_number"] == search_input:
                    print(item)
        elif view_menu_input == "3":
            search_input = input("Search Email Address:")
            for item in data:
                result = []
                if item["email"] == search_input:
                    print(item)

    elif menu_input == "2":
        print("Add New Item")
        name_input = input("Name:")
        contact_input = input("Contact Number:")
        email_input = input("Email Address:")
        
        #####
        data.append({"name":name_input,"contact_number":contact_input,"email":email_input})
    
        confirmation = input("do you want save the record ? y/n:")
        if confirmation == "y":
            with open(json_file_path, 'w') as file:
                json.dump(data,file)
        else:
            data.pop()
    elif menu_input == "3":
        use = False
    else:
        pass

