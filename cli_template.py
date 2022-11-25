#!/usr/bin/env python
import os

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
    print('commands:\nhelp - print this menu to list available commands\nclear, c - clear the screen\nquit, q, exit - exit the CLI')

def main():
    flush_screen()
    main_menu()
    while True:
        command = input('>')
        if command == 'help':
            main_menu()
        elif command == 'c' or command == 'clear':
            flush_screen()
        elif command == 'quit' or command == 'q' or command == 'exit':
            flush_screen()
            exit()
        else:
            print("Invalid command")

main()
