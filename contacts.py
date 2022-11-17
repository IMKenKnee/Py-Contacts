# importing library with csv modules
import csv

# FILENAME
# The .csv file used for file input -> held in variable FILENAME
FILENAME = "contacts.csv"

# Write Contact()
# Function that opens FILENAME and uses csv.writer object to write to .csv file
def write_contact(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        # populating row in .csv passed in from add() function
        writer.writerows(contacts)

# read_contact()
# function that uses a reader object to read in rows from .csv and creates a list to store them
def read_contact():
    # new list for contacts
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    # return method to return contacts list to global scope
    return contacts

# list_contact(contacts)
# Function to create a numbered list for terminal output to tell user contact options -> add contacts list to scope
def list_contact(contacts):
    # loop until end of list "len(contacts)"
    for i in range(len(contacts)):
        cont = contacts[i]
        print(str(i+1) + ". " + cont[0])
    print()

# add(contacts)
# Function to prompt user for input -> add contacts to scope
def add(contacts):
    # Create variables to hold contact information and populate them with user input
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    # new temporary list to hold the values -> populate list
    New = []
    New.append(name)
    New.append(email)
    New.append(phone)
    # append "New" list to contacts list
    contacts.append(New)
    # write list to .csv
    write_contact(contacts)
    print(name + " was added.\n")

# View(contacts)
# A function to view numbered list of the contents of contacts to user -> add contacts list to scope
def view(contacts):
    # prompted command that holds variable from user input
    number = int(input("Contact number: "))
    # length is equal to the length of contacts list
    length = int(len(contacts))
    # verify contact number given exists in list
    if number < 1 or number > length:
        print("Invalid contact number. Please use a number of 1 through", length , "\n")
    else:
        # print result of number given by user
        printNum = contacts[number-1]
        print("Name: ", printNum[0])
        print("E-Mail: ", printNum[1])
        print("Phone number: ", printNum[2])

# delete(contacts)
# Function that deletes a specific row from contacts list, baed on user input -> add contacts list to scope
def delete(contacts):
    # prompted command that holds variable from user input
    number = int(input("Contact number: "))
    # length is equal to the length of contacts list
    length = int(len(contacts))
    # verify contact number given exists in list
    if number < 1 or number > length:
        print("Invalid contact number. Please use a number of 1 through", length , "\n")
    else:
        # delete specific row from the list then .csv file
        with open(FILENAME, "w", newline="") as file:
            # creating writer object
            writer = csv.writer(file)
            delNum = contacts[number-1]
            print(delNum[0], "contact is now deleted.")
            # delete elements from .csv
            contacts.remove(delNum)
            # repopulates the .csv file with the updates list
            write_contact(contacts)
            
        
# display_menu()
# Function that creates a very simple menu with print funtions for the user
def display_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()

# main()
# creates the main menu for the program -> calls menu function -> reads file -> waits for user prompt with if-elif-else statement.
def main():
    display_menu()
    contacts = read_contact()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_contact(contacts)
        elif command.lower() == "view":
            view(contacts)
        elif command.lower() == "add":
            add(contacts)
        elif command.lower() == "del":
            delete(contacts)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again. \n")
    print("Bye!")

if __name__ == "__main__":
    main()
