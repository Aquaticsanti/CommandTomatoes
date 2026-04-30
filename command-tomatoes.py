from readchar import readkey, key
import shutil
import win32gui, win32con
import time
from termcolor import colored

def red(str: str) -> str:
    """Returns a given string in RED color, using the colored module from termcolor"""
    return colored(str, "red").strip()

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

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,200,260,0)
time.sleep(0.5)
cols, rows = shutil.get_terminal_size()

#print(f"columns: {cols} - rows: {rows}")
while cols != 48 and rows != 10:
    cols, rows = shutil.get_terminal_size()
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
print("")
# Screen zero: Pomodoro timer (default 25 mins)
# Screen one: Short break (default 5 mins)
# Screen two: Long break (default 15 mins)
# Screen three: Settings
screen = 0

while True:
    if screen == 0:
        print(f"""
╔══════════════════════════════════════════════╗
║{red("█")}{white("████")}{red("███")}{white("████")}{red("██")}{white("█")}{red("███")}{white("█")}{red("██")}{white("████")}{red("█")}{red("█")}                   ║
║{red("█")}{white("█")}{red("███")}{white("█")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}{white("██")}{red("█")}{white("██")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}                   ║
║{red("█")}{white("████")}{red("██")}{white("█")}{red("████")}{white("█")}{red("█")}{white("█")}{red("█")}{white("█")}{red("█")}{white("█")}{red("█")}{white("█")}{red("████")}{white("█")}{red("█")}    FOCUS BLOCK    ║
║{red("█")}{white("█")}{red("██████")}{white("████")}{red("██")}{white("█")}{red("███")}{white("█")}{red("██")}{white("████")}{red("█")}{red("█")}       MM:SS       ║
║{red("█")}{white("████")}{red("███")}{white("████")}{red("██")}{white("████")}{red("███")}{white("████")}{red("█")}{red("█")} {gray("(not started yet)")} ║
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
║{light_blue("█████")}{white("█")}{light_blue("█")}{white("█")}{light_blue("██")}{white("█")}{light_blue("██")}{white("███")}{light_blue("██")}{white("█")}{light_blue("██")}{white("█")}{light_blue("██")}{white("██")}{light_blue("█")}       MM:SS       ║
║{light_blue("█")}{white("████")}{light_blue("██")}{white("███")}{light_blue("██")}{white("█████")}{light_blue("██")}{white("██")}{light_blue("██")}{white("█")}{light_blue("█")}{white("██")} {gray("(not started yet)")} ║
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
║{blue("█")}{white("█████")}{blue("███")}{white("███")}{blue("███")}{white("█")}{blue("██")}{white("█")}{blue("███")}{white("███")}{blue("██")}       MM:SS       ║
║{blue("█")}{white("████")}{blue("██")}{white("███")}{blue("██")}{white("█████")}{blue("██")}{white("██")}{blue("██")}{white("█")}{blue("█")}{white("██")} {gray("(not started yet)")} ║
║{blue("█")}{white("█")}{blue("███")}{white("█")}{blue("█")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("█")}{blue("█████")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("██")}{blue("██")}                   ║
║{blue("█")}{white("████")}{blue("██")}{white("███")}{blue("██")}{white("███")}{blue("███")}{white("████")}{blue("█")}{white("██")}{blue("██")}                   ║
║{blue("█")}{white("████")}{blue("██")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("█████")}{blue("█")}{white("█")}{blue("██")}{white("█")}{blue("█")}{white("█")}{blue("█")}{white("██")}    {gray("< Page 3/4 >")}   ║
╚══════════════════════════════════════════════╝""", end="")
    elif screen == 3:
        print("""
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║    Uh oh, looks like this is not ready       ║
║         yet! Please come back later          ║
║                 (Page 4)                     ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝""", end="")
    k = readkey()
    if k == key.LEFT:
        screen -= 1
        if screen < 0:
            screen = 3
    elif k == key.RIGHT:
        screen += 1
        if screen > 3:
            screen = 0

# Cool box divider: ╔════════╗
#                   ║        ║ Source: https://gist.github.com/jamiew/40c66061b666272462c17f65addb14d5
#                   ╚════════╝