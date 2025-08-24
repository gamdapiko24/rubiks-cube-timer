# main.py

import scrambler
from stats import Commands
import timedictgen as tdg
from datetime import datetime

def f_time(now):
    return f'{now.month}-{now.day}-{now.year} {now.hour}:{now.minute}:{now.second}'

def command_line():
    cmd = Commands(timedata[event])
    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == 'quit':
            global timer
            timer = False
            break
        if user_input.lower() == 'no':
            break
        result = cmd.execute(user_input)
        if result:
            print(result)
            if 'Unknown command' not in result:
                break

timedata = tdg.get_data()
if timedata is None:
    timedata = tdg.timedata

print("Welcome to Lui's Cube Timer!")
event = input("What Rubik's Cube event are you timing?").strip()
while not event in timedata:
    if event == 'commands':
        event = input('Choose an event to use for commands').strip()
        while True:
            command_line()
    temp = input(f'It seems like this event is not on the list. \
Would you like to add {event}? (y/n)').strip()
    if temp == 'y':
        timedata[event] = tdg.dperevent
    else:
       event = input("What Rubik's Cube event are you timing?").strip()
    

timer = True

def main_loop():
    global timedata
    if event == '3x3':
        scramble = scrambler.scramble3x3(20)
    print(scramble)
    while True:
        temp = input('Enter your time or DNF: ').strip()
        if temp.upper() == 'DNF':
            time = 'DNF'
            break
        try:
            time = float(temp)
            break
        except ValueError:
            print('Please enter a number or DNF')
    now = datetime.now()
    timedata = tdg.addtime(timedata,event,f_time(now),time,scramble,input('Any comments?').strip())
    tdg.save_data(timedata)

while timer:
    main_loop()
    command_line()
