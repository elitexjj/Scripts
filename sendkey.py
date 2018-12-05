import sys
import msvcrt
from pynput.keyboard import Key,Controller
from time import sleep

string = sys.argv[1];
mode = sys.argv[2];
keyboard = Controller();

sleep(3);

if mode == "once":
    keyboard.type(string);
    exit();
elif mode == "command":
    keyboard.type(string);
    keyboard.press(Key.enter);
    exit();
elif mode == "infinite":
    pass

while True:
    sleep(0.1);
    keyboard.type(string);