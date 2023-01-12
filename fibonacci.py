#!/usr/bin/env python

s = 1
t = 1
e = 0
fibo_log = []

def fibo_range(num):
    global s
    global t
    global e
    global fibo_log
    if num >= 1:
        fibo_log.append(s)
        if num >= 2:
            fibo_log.append(t)
            if num >= 3:
                for i in range(num - 2):
                    e = s + t
                    fibo_log.append(e)
                    s = t
                    t = e
    return fibo_log

def fibo_search(num):
    global s
    global t
    global e
    global fibo_log
    seq = []
    fibo_log.append(s)
    fibo_log.append(t)
    if num >= 3:
        for i in range(num):
            e = s + t
            fibo_log.append(e)
            s = t
            t = e
    for j in fibo_log:
        seq.append(j)
        if j == num:
            result = "I found it!\nThe number " + str(j) +  " does in fact exist in the Fibonacci sequence,\nhere is the Fibonacci sequence up until that number:\n" + str(seq)
            return result
        else:
            continue
    result = "I calculated the Fibonacci sequence for an amount of numbers equal to the number you gave me, but as you can see here:\n" + str(seq) + "\nSadly that number is not in the Fibonacci sequence :("
    return result

user_choice = input("Heya, I'm your personal Fibonacci assistant :)\nI can calculate the Fibonacci sequence to any amount of numbers you want!\nThere is several ways I can do this:\n1. You give me an integer and I use that as the limit to which I calculate the sequence, so for example you say 3 and I will calculate 3 numbers in the sequence\n2. You give me an integer and I calculate the Fibonacci sequence to that integer amount of numbers and see if that integer exists in the sequence or not\nWhat would you like me to do? (1/2)\n>")
running = True
while running:
    if user_choice == "1":
        print(fibo_range(int(input("How many numbers of the Fibonacci sequence would you like to calculate?\n>"))))
        running = False
    elif user_choice == "2":
        print(fibo_search(int(input("enter an integer to see if it exists in the Fibonacci sequence\n>"))))
        running = False
    else:
        user_choice = input("That number is not one of the options I gave you, can you please choose either 1 or 2?")
