import serial 
import os

ser = serial.Serial('/dev/ttyACM0', 11500, timeout=0.01)

# get character input without pressing enter
def getch():
    import sys, termios

    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)

    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0

    try:
        termios.tcsetattr(fd, termios.TCSAFLUSH, new)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)

# menu
def setting():
    menu = ""
    while menu != "x":
        os.system("clear")
        print("--- Menu ---")
        menu = input()
    
    os.system("clear")


while 1:
    command = getch()

    # open setting menu
    if command == "x":
        setting()

    ser.write(command.encode('UTF-8'))
    picoData = ser.readline()
    print(picoData)
