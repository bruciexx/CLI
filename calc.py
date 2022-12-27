#!/usr/bin/env python

import argparse as ap

p = ap.ArgumentParser(description='A simple CLI calculator')
p.add_argument('-command', '-c', help='operation name: a, s, m or d for Add, Subtract, Multiply and Divide')
p.add_argument('-int1', '-i1', type=float, help='value one (float)')
p.add_argument('-int2', '-i2', type=float, help='value two (float)')
p.add_argument('-ping', '-p', action='store_true', help='pong')
arg = p.parse_args()

if arg.ping:
    print('pong')
    exit()
else:
    if arg.command == 'add' or arg.command == 'a':
        print(arg.int1 + arg.int2)
    elif arg.command == 'sub' or arg.command == 's':
        print(arg.int1 - arg.int2)
    elif arg.command == 'mul' or arg.command == 'm':
        print(arg.int1 * arg.int2)
    elif arg.command == 'div' or arg.command == 'd':
        print(arg.int1 / arg.int2)
    else:
        print('command unavailable')

