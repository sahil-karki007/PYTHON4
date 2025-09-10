data = {}

def display(data):
    if not data:
        print("No Contacts Found")
    else:
        print("Contact List")
        for name , number in data.items():
            print(f"Name: {name} , Phone No.: {number}")

def add(data , name , number):
    data[name] = number
    print(f"Contact {name} added successfully")

def update(data , name , number):
    if name in data:
        data[name] = number
        print(f"Contact {name} updated successfully")

def delete(data , name):
    if name in data:
        del data[name]
        print(f"Contact {name} deleted successfully")

def search(data , name):        
    if name in data:
        print(f"Found\n Name: {name} , Phone number: {number}")
    else:
        print("Contact not found")

    
while True:
    print("==== CONTACT BOOK ====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    a = input("Enter your choice: ")

    if a == "1":
        name = input("Enter Name: ").lower()
        number = int(input("Enter Phone No.: "))
        add(data , name , number)

    elif a == "2":
        display(data)
        
    elif a == "3":
        name = input("Enter name to search: ").lower()
        search(data , name)

    elif a == "4":
        name = input("Enter name to update: ").lower()
        number = int(input("Enter phone no. to update: "))
        update(data , name , number)

    elif a == "5":
        name = input("Enter name to delete: ").lower()
        delete(data , name)

    elif a == "6":
        print("Exiting contact book...\nGOODBYE!!!")
        break

    else:
        print("Invalid choice")    