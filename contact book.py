def add_contact(contact_list,name,phn_no,email,add):
    contact_list[phn_no]={
        "Name":name,
        "Phone Number":phn_no,
        "Email":email,
        "Address":add
    }
    print(f"Contact for '{name}' added succesfully!\n")

def view_contacts(contact_list):
    if not contact_list:
        print("No contacts available.\n")
        return
    else:
        print("\n--- Contact List ---")
        for contact in contact_list.values():
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print("----------------------------")
        print()

def search_contact(contact_list,keyword):
    if not contact_list:
        print("No contact details available")
    else:
        for contact in contact_list.values():
            if keyword.title()==contact['Name'].title() or keyword==str(contact['Phone Number']):
                print(f"Name: {contact['Name']}")
                print(f"Phone Number: {contact['Phone Number']}")
                print(f"Email: {contact['Email']}")
                print(f"Address: {contact['Address']}")
                print("----------------------------\n")

def update_contact(contact_list,phn_no):
    if phn_no in contact_list:
        print(f"\nUpdating contact for {contact_list[phn_no]['Name']}:")
        new_name = input("Enter new Name: ")
        new_phone_number = input("Enter new Phone Number: ")
        new_email = input("Enter new Email: ")
        new_address = input("Enter new Address: ")
        
        # Delete old entry if phone number is changed
        if new_phone_number != phn_no:
            del contact_list[phn_no]
        
        contact_list[new_phone_number] = {
            "Name": new_name,
            "Phone Number": new_phone_number,
            "Email": new_email,
            "Address": new_address
        }
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact(phn_no):
    if phn_no in contact_list:
        del contact_list[phn_no]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

        
contact_list={}
def main():
    print("------CONTACT BOOK------")
    print("1. Add contacts")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    while True:
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter your name: ")
            phn_no=int(input("Enter your phone number: "))
            email=input("Enter your email: ")
            add=input("Enter your address: ")
            add_contact(contact_list,name,phn_no,email,add)
        elif choice==2:
            view_contacts(contact_list)
        elif choice==3:
            keyword=input("Enter name or phone number to search: ")
            search_contact(contact_list,keyword)
        elif choice==4:
            phn_no = int(input("Enter the Phone Number of the contact to update: "))
            update_contact(contact_list,phn_no)
        elif choice==5:
            phn_no = int(input("Enter the Phone Number of the contact to delete: "))
            delete_contact(phn_no)
        elif choice==6:
            print("Exit")
            break
        else:
            print("Invalid choice")
        
if __name__=="__main__":
    main()