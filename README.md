Lead Management System (LMS)

This Python script implements a basic Lead Management System (LMS) using a JSON file to store lead information. The script provides functionality to view existing leads, add new leads, and exit the program. 
It utilizes the tabulate library to present data in a tabular format.

Dependecies
Tabulate: The script uses the tabulate library to display data in a table format. 
Run this code: pip intall tabulate

File Structure
- lms.json: This JSON file serves as the data storage for lead information. It is initially loaded and updated as new leads are added.
- lead_management.py: The main Python script containing the LMS functionality.

How to Use
1. Viewing Existing Leads: Enter '1' when prompted for the menu input. You can then choose to search for leads by name, contact number, or email address.
2. Adding a New Lead: Enter '2' when prompted for the menu input. Provide the necessary information for the new lead, including name, contact number, and email address. Confirm whether you want to save the record.
3. Exiting the Program: Enter '3' when prompted for the menu input to exit the program.

