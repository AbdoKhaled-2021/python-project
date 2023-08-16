import csv
import os
from datetime import datetime

class Contact:
    def _init_(self, username, email, phone_numbers, address):
        self.username = username
        self.email = email
        self.phone_numbers = phone_numbers
        self.address = address
        self.insertion_date = datetime.now().strftime('%d%m%Y')

class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def update_contact(self, username, updated_contact):
        for contact in self.contacts:
            if contact.username == username:
                contact.email = updated_contact.email
                contact.phone_numbers = updated_contact.phone_numbers
                contact.address = updated_contact.address
                break

    def delete_contact(self, username):
        self.contacts = [contact for contact in self.contacts if contact.username != username]

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Username', 'Email', 'Phone Numbers', 'Address', 'Insertion Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({
                    'Username': contact.username,
                    'Email': contact.email,
                    'Phone Numbers': ', '.join(contact.phone_numbers),
                    'Address': contact.address,
                    'Insertion Date': contact.insertion_date
                })

def main():
    contact_book = ContactBook()
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Save Contacts to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Username: ")
            email = input("Email: ")
            phone_numbers = input("Phone Numbers (comma-separated): ").split(',')
            address = input("Address: ")
            contact = Contact(username, email, phone_numbers, address)
            contact_book.add_contact(contact)
            print("Contact added.")

        elif choice == '2':
            username = input("Enter username of contact to update: ")
            updated_email = input("New Email: ")
            updated_phone_numbers = input("New Phone Numbers (comma-separated): ").split(',')
            updated_address = input("New Address: ")
            updated_contact = Contact(username, updated_email, updated_phone_numbers, updated_address)
            contact_book.update_contact(username, updated_contact)
            print("Contact updated.")

        elif choice == '3':
            username = input("Enter username of contact to delete: ")
            contact_book.delete_contact(username)
            print("Contact deleted.")

        elif choice == '4':
            filename = f"contactbook_{datetime.now().strftime('%d%m%Y')}.csv"
            contact_book.save_to_csv(filename)
            print(f"Contacts saved to {filename}.")

        elif choice == '5':
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if _name_ == "_main_":
    main()