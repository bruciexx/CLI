#!/usr/bin/env python
import time
import argparse as ap
from beepy import beep
def clear():
    print("\033c", end="")

class Timer:
    def __init__(self, start = 0, sec = 30, min = 0, hour = 0):
        self.start = start
        self.sec = sec + min * 60 + hour * 60 * 60
        self.min = sec / 60 + min + hour * 60
        self.hour = sec / (60*60) + min / 60 + hour
        self.end_time = sec
        self.time_up = False
        self.ms = 0
        self.hr = 0
        self.mn = 0
        self.counter = 0

    def print_time(self):
        if self.counter < 10:
            if self.mn < 10:
                print(f'00:0{self.mn}:0{self.counter}:{self.ms}')
            else:
                print(f'00:{self.mn}:0{self.counter}:{self.ms}')
        else:
            if self.mn < 10:
                print(f'00:0{self.mn}:{self.counter}:{self.ms}')
            else:
                print(f'00:{self.mn}:{self.counter}:{self.ms}')

    def count(self):
        while self.time_up == False:
            if self.start == self.end_time:
                self.time_up == True
                self.ms = 0
                break
            else:
                pass
            clear()
            while self.counter < 60:
                self.ms = 0
                for i in range(1000):
                    clear()
                    self.print_time()
                    self.ms += 1
                    time.sleep(0.001)
                self.counter += 1
                self.start += 1
            self.mn += 1
            self.counter = 0
        clear()
        if self.hour < 1:
            if self.min < 1:
                self.print_time()
            else:
                self.print_time()
        else:
            pass
        print("Timer finished")
        beep(sound=4)

p = ap.ArgumentParser(description='A simple CLI calculator')
p.add_argument('-sec', '-s', default=10, type=int)
arg = p.parse_args()

timer_standard = Timer(0, arg.sec)
timer_standard.count()
