import json

json_file_path = "python-lead-management/lms.json"

with open(json_file_path, 'r') as file:
    data = json.load(file)


for item in data:
    for key, value in item.items():
        print(f"{key} : {value}")
        


