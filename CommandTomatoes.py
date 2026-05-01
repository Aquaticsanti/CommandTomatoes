from readchar import readkey, key
import shutil
import win32gui, win32con
import time
import datetime
import threading
from termcolor import colored
import argparse

parser = argparse.ArgumentParser(
                    prog='CommandTomatoes',
                    description='A Pomodoro Timer for your Command Line! (To start without options, use no arguments.)')
parser.add_argument("-f", "--focus-time", default=25, type=float,
                    help="Set the time for the focus block, formated as a float of 'minutes.seconds'.Defaults to 25 mins.")
parser.add_argument("-s", "--short-break-time", default=5, type=float,
                    help="Set the time for the short break block, formated as a float of 'minutes.seconds' Defaults to 5 mins.")
parser.add_argument("-l", "--long-break-time", default=15, type=float,
                    help="Set the time for the long break block, formated as a float of 'minutes.seconds' Defaults to 15 mins.")

args = vars(parser.parse_args())

def red(str: str) -> str:
    """Returns a given string in RED color, using the colored module from termcolor"""
    return colored(str, "red")

def white(str: str) -> str:
    """Returns a given string in WHITE color, using the colored module from termcolor"""
    return colored(str, "white")

def blue(str: str) -> str:
    """Returns a given string in BLUE color, using the colored module from termcolor"""
    return colored(str, "blue")

def light_blue(str: str) -> str:
    """Returns a given string in LIGHT BLUE color, using the colored module from termcolor"""
    return colored(str, "light_blue")

def gray(str: str) -> str:
    """Returns a given string in DARK GRAY color, using the colored module from termcolor"""
    return colored(str, "dark_grey")

def light_cyan(str: str) -> str:
    """Returns a given string in LIGHT CYAN color, using the colored module from termcolor"""
    return colored(str, "light_cyan")

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,200,260,0)
time.sleep(0.5)
cols, rows = shutil.get_terminal_size()

focusLength = datetime.timedelta(minutes=int(args["focus_time"]), seconds=int(str(float(args["focus_time"])-int(args["focus_time"]))[2:]))
shortBreakLenght = datetime.timedelta(minutes=int(args["short_break_time"]), seconds=int(str(float(args["short_break_time"])-int(args["short_break_time"]))[2:]))
longBreakLenght = datetime.timedelta(minutes=int(args["long_break_time"]), seconds=int(str(float(args["long_break_time"])-int(args["long_break_time"]))[2:]))
elapsedSec = 0

#print(f"columns: {cols} - rows: {rows}")
while cols != 48 and rows != 10:
    print("""
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║    Uh oh, looks like this terminal is not    ║
║                   48x10                      ║
║   Please adjust the zoom (Ctrl + or Ctrl -)  ║
║    until this square fits in the terminal    ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝""", end="")
    while cols != 48 and rows != 10:
        cols, rows = shutil.get_terminal_size()
print("")
# Screen zero: Pomodoro timer (default 25 mins)
# Screen one: Short break (default 5 mins)
# Screen two: Long break (default 15 mins)
# Screen three: Settings
screen = 0
selectedSettings = 0
started = None
paused = None

def keyread():
    global screen, started, paused, elapsedSec, selectedSettings
    k = readkey()
    if k == key.LEFT:
        if paused == True or started == None:
            elapsedSec = 0
            screen -= 1
            if screen < 0:
                screen = 3
    elif k == key.RIGHT:
        if paused == True or started == None:
            elapsedSec = 0
            screen += 1
            if screen > 3:
                screen = 0
    elif k == key.SPACE:
        if started == True:
            if paused == True:
                paused = False
            else:
                paused = True
        else:
            started = True
            paused = False
    
def ElapsedTime():
    global elapsedSec
    time.sleep(1)
    elapsedSec += 1

def PreventNegativeTime():
    global elapsedSec, started, paused
    if (focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds() <= 0 or (shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() <= 0 or (longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() <= 0:
        elapsedSec = 0
        started = None
        paused = None

keyThread = threading.Thread(target=keyread)
timeThread = threading.Thread(target=ElapsedTime)
PreventNegativeTimeThread = threading.Thread(target=PreventNegativeTime)

while True:
    if screen == 0:
        print(f"""
╔══════════════════════════════════════════════╗
║{red("█")}{white("████")}{red("███")}{white("████")}{red("██")}{white("█")}{red("███")}{white("█")}{red("██")}{white("████")}{red("█")}{red("█")}                   ║
║{red("█")}{white("█")}{red("███")}{white("█")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}{white("██")}{red("█")}{white("██")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}                   ║
║{red("█")}{white("████")}{red("██")}{white("█")}{red("████")}{white("█")}{red("█")}{white("█")}{red("█")}{white("█")}{red("█")}{white("█")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}    FOCUS BLOCK    ║
║{red("█")}{white("█")}{red("██████")}{white("████")}{red("██")}{white("█")}{red("███")}{white("█")}{red("██")}{white("████")}{red("█")}{red("█")}       {f"{int(int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds()) // 60)}:{int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60 if len(str(int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60)) == 2 else f"0{int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60}"}"}       ║
║{red("█")}{white("████")}{red("███")}{white("████")}{red("██")}{white("████")}{red("███")}{white("████")}{red("█")}{red("█")} {gray(f"{"(not started yet)" if started == None else "    (ongoing)    " if paused == False else "     (paused)    "}")} ║
║{red("█")}{white("█")}{red("███")}{white("█")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}{white("█")}{red("███")}{white("█")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}                   ║
║{red("█")}{white("█")}{red("███")}{white("█")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}{white("████")}{red("██")}{white("█")}{red("████")}{white("█")}{red("█")}                   ║
║{red("█")}{white("████")}{red("███")}{white("████")}{red("██")}{white("█")}{red("███")}{white("█")}{red("██")}{white("████")}{red("█")}{red("█")}    {gray("< Page 1/4 >")}   ║
╚══════════════════════════════════════════════╝""", end="")
    elif screen == 1:
        print(f"""
╔══════════════════════════════════════════════╗
║{light_blue("█")}{white("█████")}{light_blue("█")}{white("█")}{light_blue("██")}{white("█")}{light_blue("██")}{white("███")}{light_blue("██")}{white("███")}{light_blue("██")}{white("████")}                   ║
║{light_blue("█")}{white("█")}{light_blue("█████")}{white("████")}{light_blue("█")}{white("█")}{light_blue("███")}{white("█")}{light_blue("█")}{white("█")}{light_blue("██")}{white("█")}{light_blue("██")}{white("██")}{light_blue("█")}                   ║
║{light_blue("█")}{white("█████")}{light_blue("█")}{white("████")}{light_blue("█")}{white("█")}{light_blue("███")}{white("█")}{light_blue("█")}{white("███")}{light_blue("███")}{white("██")}{light_blue("█")}    SHORT BREAK    ║
║{light_blue("█████")}{white("█")}{light_blue("█")}{white("█")}{light_blue("██")}{white("█")}{light_blue("██")}{white("███")}{light_blue("██")}{white("█")}{light_blue("██")}{white("█")}{light_blue("██")}{white("██")}{light_blue("█")}       {f"{int(((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds()) // 60)}:{int(((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60) if len(str(int(((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60))) == 2 else f"0{int(((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60)}"}"}        ║
║{light_blue("█")}{white("████")}{light_blue("██")}{white("███")}{light_blue("██")}{white("█████")}{light_blue("██")}{white("██")}{light_blue("██")}{white("█")}{light_blue("█")}{white("██")} {gray(f"{"(not started yet)" if started == None else "    (ongoing)    " if paused == False else "     (paused)    "}")} ║
║{light_blue("█")}{white("█")}{light_blue("███")}{white("█")}{light_blue("█")}{white("█")}{light_blue("██")}{white("█")}{light_blue("█")}{white("█")}{light_blue("█████")}{white("█")}{light_blue("██")}{white("█")}{light_blue("█")}{white("██")}{light_blue("██")}                   ║
║{light_blue("█")}{white("████")}{light_blue("██")}{white("███")}{light_blue("██")}{white("███")}{light_blue("███")}{white("████")}{light_blue("█")}{white("██")}{light_blue("██")}                   ║
║{light_blue("█")}{white("████")}{light_blue("██")}{white("█")}{light_blue("██")}{white("█")}{light_blue("█")}{white("█████")}{light_blue("█")}{white("█")}{light_blue("██")}{white("█")}{light_blue("█")}{white("█")}{light_blue("█")}{white("██")}    {gray("< Page 2/4 >")}   ║
╚══════════════════════════════════════════════╝""", end="")
    elif screen == 2:
        print(F"""
╔══════════════════════════════════════════════╗
║{blue("█")}{white("█")}{blue("███████")}{white("███")}{blue("███")}{white("█")}{blue("██")}{white("█")}{blue("███")}{white("███")}{blue("██")}                   ║
║{blue("█")}{white("█")}{blue("██████")}{white("█")}{blue("███")}{white("█")}{blue("██")}{white("██")}{blue("█")}{white("█")}{blue("██")}{white("█")}{blue("█████")}                   ║
║{blue("█")}{white("█")}{blue("██████")}{white("█")}{blue("███")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("██")}{blue("██")}{white("█")}{blue("██")}{white("███")}     LONG BREAK    ║
║{blue("█")}{white("█████")}{blue("███")}{white("███")}{blue("███")}{white("█")}{blue("██")}{white("█")}{blue("███")}{white("███")}{blue("██")}       {f"{int(((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds()) // 60)}:{int((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60) if len(str(int((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60))) == 2 else f"0{int((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60)}"}"}       ║
║{blue("█")}{white("████")}{blue("██")}{white("███")}{blue("██")}{white("█████")}{blue("██")}{white("██")}{blue("██")}{white("█")}{blue("█")}{white("██")} {gray(f"{"(not started yet)" if started == None else "    (ongoing)    " if paused == False else "     (paused)    "}")} ║
║{blue("█")}{white("█")}{blue("███")}{white("█")}{blue("█")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("█")}{blue("█████")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("██")}{blue("██")}                   ║
║{blue("█")}{white("████")}{blue("██")}{white("███")}{blue("██")}{white("███")}{blue("███")}{white("████")}{blue("█")}{white("██")}{blue("██")}                   ║
║{blue("█")}{white("████")}{blue("██")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("█████")}{blue("█")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("█")}{blue("█")}{white("██")}    {gray("< Page 3/4 >")}   ║
╚══════════════════════════════════════════════╝""", end="")
    elif screen == 3:
        print(f"""
╔══════════════════════════════════════════════╗
║{light_cyan("███████████████████████████")}      SETTINGS     ║
║{light_cyan("████████")}{white("██")}{light_cyan("██")}{white("██")}{light_cyan("██")}{white("██")}{light_cyan("█████████")}                   ║
║{light_cyan("██████████")}{white("██████")}{light_cyan("███████████")} FOCUS BLOCK: {f"{f"{int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds() // 60)}:{int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60 if len(str(int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60)) == 2 else f"0{int((focusLength - datetime.timedelta(seconds=elapsedSec)).total_seconds()) % 60}"}"}"}║
║{light_cyan("████████")}{white("████")}{light_cyan("██")}{white("████")}{light_cyan("█████████")} SHORT BREAK: {f"{int((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() // 60)}:{int((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60) if len(str(int((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60))) == 2 else f"0{int((shortBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60)}"}"} ║
║{light_cyan("██████████")}{white("██████")}{light_cyan("███████████")} LONG BREAK: {f"{int((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() // 60)}:{int((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60) if len(str(int((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60))) == 2 else f"0{int((longBreakLenght - datetime.timedelta(seconds=elapsedSec)).total_seconds() % 60)}"}"} ║
║{light_cyan("████████")}{white("██")}{light_cyan("██")}{white("██")}{light_cyan("██")}{white("██")}{light_cyan("█████████")}                   ║
║{light_cyan("███████████████████████████")}                   ║
║{light_cyan("███████████████████████████")}    {gray("< Page 4/4 >")}   ║
╚══════════════════════════════════════════════╝""", end="")
    
    while keyThread.is_alive() == True and timeThread.is_alive() == True and PreventNegativeTimeThread.is_alive() == True:
        pass
    if keyThread.is_alive() == False:
        keyThread = threading.Thread(target=keyread)
        keyThread.start()
    if timeThread.is_alive() == False and paused == False:
        timeThread = threading.Thread(target=ElapsedTime)
        timeThread.start()
    if PreventNegativeTimeThread.is_alive() == False:
        PreventNegativeTimeThread = threading.Thread(target=PreventNegativeTime)
        PreventNegativeTimeThread.start()
# Cool box divider: ╔════════╗
#                   ║        ║ Source: https://gist.github.com/jamiew/40c66061b666272462c17f65addb14d5
#                   ╚════════╝