#!/usr/bin/env python
import os

data = []

def line():
    t_size = os.get_terminal_size()
    t_width = t_size.columns
    print(t_width * "-")

def flush_screen():
    print('\033c', end="")

def main_menu():
    line()
    print('Main menu')
    line()
    print('commands:\nuseradd - (Add a new user to the phonebook)\nuserdel - (Delete a user from the phonebook based on the first name of the user\nlistusers - List all the users in the phonebook\n')

def user_add(name_first, name_last, email, phone):
    global data
    new_user = {'first_name': '', 'last_name': '', 'email': '', 'phone': ''}
    new_user.update({'first_name': name_first, 'last_name': name_last, 'email': email, 'phone': phone})
    data.append(new_user)
    print(new_user)

def user_remove(search_query):
    for user in data:
        index = data.index(user)
        if search_query in user.values():
            del data[index]

def list_users():
    data_index = 0
    for user in data:
        line()
        data_index += 1
        itrn = 0
        for value in user.values():
            if itrn == 0:
                print("First name:", value)
            elif itrn == 1:
                print("Last name:", value)
            elif itrn == 2:
                print("Email:", value)
            elif itrn == 3:
                print("Phone:", value)
            else:
                exit()
            itrn += 1

def main():
    user_add("Bruce", "Gooijer", "brucegooijer@gmail.com", "0641182212")
    flush_screen()
    main_menu()
    while True:
        command = input('>')
        if command == 'useradd':
            print("Adding new user...")
            first_name = input("What is the user's first name? >")
            last_name = input("What is the user's last name? >")
            email = input("What is the user's email? >")
            phone = input("What is the user's phone number? >")
            user_add(first_name, last_name, email, phone)
        elif command == 'userdel':
            print("Deleting existing user...")
            query = input("What user would you like to delete? >")
            user_remove(query)
        elif command == 'listusers':
            print("The users in the phone book are: ")
            list_users()
        elif command == 'help':
            main_menu()
        elif command == 'c' or command == 'clear':
            flush_screen()
        elif command == 'quit' or command == 'q' or command == 'exit':
            flush_screen()
            exit()
        else:
            print("Invalid command")

main()
