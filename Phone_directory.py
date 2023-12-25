print("***************************************Welcome to udaydinesh's Phone Book************************************************")

contact={}

print(''' Choose any one option :
       1. Add new contact
       2. Update existing contact
       3. Delete contact
       4. Search contact
       5. Show all contact
       6. Exit the contact book
       ''') #here choose any one option so it will move forward
       
def add():
    nam=input("Enter Name: ") #your name
    num=int(input("Enter Phone Number: ")) #your phone number
    if nam in contact:
        print("Contact alredy exists you want to add")
    else:
        contact[nam]=num
        option=input("Want to add more y/n: ")
        if option=='y':
            add() 
        else:
            print("okay contacts saved successfully")

def update():
    nam2=input("Enter Name you want to update: ") 
    if nam2 in contact:
        num2=int(input("Enter Updated Number: ")) 
        contact[nam2]=num2
        print("contact updated!!")
        option2=input("Want to update more contact y/n: ") 
        if option2=='y':
            update() 
        else:
            print("Getting Ahead")
    else:
        print("Name you entered dosen't exist go to 'Add new contact' option from menu below")

def delete():
    nam3=input("Enter Name you want to delete: ") 
    if nam3 in contact:
        contact.pop(nam3) 
        print("Contact deleted")
        option3=input("Want to delete more contact y/n: ") 
        if option3=='y':
            delete() 
        else:
            print("Getting Ahead") 
    else:
        print("Name dosen't exists")

def search():
    nam4=input("Enter Name you want to search: ") 
    if nam4 in contact:
        print(f"Contact name: {nam4} Number: {contact[nam4]}")
        option4=input("Want to search more contact y/n: ")
        if option4=='y': 
            search()
        else:
            print("Getting Ahead")
    else:
        print("Not in the list please add first")

def display():
    print(contact)

while(True):
    choice=int(input("Your option between 1-6: ")) 
    if choice==1:
        add()
    if choice==2: 
        update()
    if choice==3: 
        delete()
    if choice==4: 
        search()
    if choice==5: 
        display()
    if choice==6:
        print("Thanks for using Adi's Phonebook")
        break