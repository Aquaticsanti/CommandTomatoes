from readchar import readkey, key
import shutil
import win32gui, win32con
import time

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

print("""
╔══════════════════════════════════════════════╗
║                                              ║
║                                              ║
║                                              ║
║                  Size ok!                    ║
║                                              ║
║                                              ║
║                                              ║
║                                              ║
╚══════════════════════════════════════════════╝""", end="")

input()

# Cool box divider: ╔════════╗
#                   ║        ║ Source: https://gist.github.com/jamiew/40c66061b666272462c17f65addb14d5
#                   ╚════════╝