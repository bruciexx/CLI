#!/usr/bin/env python

import argparse as ap

p = ap.ArgumentParser(description='CLI template')
p.add_argument('-command', '-c', help='command description and usage')
p.add_argument('-ping', '-p', action='store_true', help='pong')
arg = p.parse_args()

if arg.ping:
    print('pong')
    exit()
if arg.command == 'test':
    print('test')
    exit()
else:
    print('command unavailable')
    exit()
