#!/usr/bin/env python

chars_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
chars_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
chars_spec = [" ", "!", '"', "'", "(", ")", "*", ",", ".", "-", "&", ":", ";", "?", "~"]

def encode(msg, key=1):
    global chars_upper
    global chars_lower
    global chars_spec
    enc_msg = ""
    for c in msg:
        if c.isupper():
            for l in chars_upper:
                if c == l:
                    num = chars_upper.index(l)
                    res = (num + key) % 26
                    enc_msg += chars_upper[res]
        elif c.islower():
            for l in chars_lower:
                if c == l:
                    num = chars_lower.index(l)
                    res = (num + key) % 26
                    enc_msg += chars_lower[res]
        else:
            for l in chars_spec:
                if c == l:
                    enc_msg += c
    return enc_msg

def decode(msg, key=1):
    global chars_upper
    global chars_lower
    global chars_spec
    dec_msg = ""
    for c in msg:
        if c.isupper():
            for l in chars_upper:
                if c == l:
                    num = chars_upper.index(l)
                    res = (num - key) % 26
                    dec_msg += chars_upper[res]
        elif c.islower():
            for l in chars_lower:
                if c == l:
                    num = chars_lower.index(l)
                    res = (num - key) % 26
                    dec_msg += chars_lower[res]
        else:
            for l in chars_spec:
                if c == l:
                    dec_msg += c
    return dec_msg


while True:
    print("\033c", end="")
    choice = input("Would you like to encode or decode a message?: ")
    if choice == 'encode' or choice == 'decode':
        msg = input("What would you like to " +  choice + "?\n>")
    else:
        print("That was not one of the options, please try again")
        continue
    key = input("What is the key(shift) you would like to use to " + choice + " the message?\n>")
    try:
        key = int(key)
    except ValueError:
        print("You can only use integers as a key to encrypt the message.\nI mean how do you expect me to move the letters by '" + key + "' amount of places?")
        continue
    if choice == 'encode':
        print(encode(msg, key), "\n")
    else:
        print(decode(msg, key), "\n")
    ch = input("again?\n")
    if ch == 'y' or ch == 'yes':
        continue
    else:
        exit(0)
