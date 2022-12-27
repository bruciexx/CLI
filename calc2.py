#!/usr/bin/env python

import argparse as ap
import sys

p = ap.ArgumentParser(description='A simple CLI calculator')
p.add_argument('-command', '-c', help='operation name: a, s, m or d for Add, Subtract, Multiply and Divide')
p.add_argument('-int1', '-i1', type=float, help='value one (float)')
p.add_argument('-int2', '-i2', type=float, help='value two (float)')
p.add_argument('-ping', '-p', action='store_true', help='pong')
arg = p.parse_args()


commands = {
        lambda a, b: a+b: ['add', 'a'],
        lambda a, b: a-b: ['sub', 's'],
        lambda a, b: a*b: ['mul', 'm'],
        lambda a, b: a/b: ['div', 'd']
        }

if arg.ping:
    print('pong')
    sys.exit(0)

for operation, command_value in commands.items():
    if arg.command in command_value:
        print(f'{operation(arg.int1, arg.int2)}')
        sys.exit(0)

print('command unavailable')
