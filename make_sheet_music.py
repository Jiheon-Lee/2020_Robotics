
import win32api
import win32con
import win32gui
import pyperclip
import sys


# KEYMAP setting(letter code)
KEYMAP = {
    # 제어 키
    "esc": 0x1B,  "window": 0x5B,
    "control": 0x11,    "alt": 0x12,  "kor_eng": 0x15,
    "print_screen": 0x2C,    "scroll_lock": 0x91,   "pause_break": 0x13,

    # 기능 키
    "f1": 0x70,    "f2": 0x71,    "f3": 0x72,    "f4": 0x73,
    "f5": 0x74,    "f6": 0x75,    "f7": 0x76,    "f8": 0x77,
    "f9": 0x78,    "f10": 0x79,    "f11": 0x7A,    "f12": 0x7B,

    # 화살표 키
    "left_arrow": 0x25,    "right_arrow": 0x27,
    "up_arrow": 0x26,    "down_arrow": 0x28,

    # 탐색 키
    "insert": 0x2D,    "home": 0x24,    "page_up": 0x21,
    "delete": 0x2E,    "end": 0x23,     "page_down": 0x22,

    # 입력 키 (편집)
    "backspace": 0x08,  "enter": 0x0D,  "shift": 0x10,
    "tab": 0x09,    "caps_lock": 0x14,  "spacebar": 0x20,

    # 입력 키 (숫자)
    "0": 0x30,    "1": 0x31,    "2": 0x32,    "3": 0x33,    "4": 0x34,
    "5": 0x35,    "6": 0x36,    "7": 0x37,    "8": 0x38,    "9": 0x39,

    # 입력 키 (알파벳)
    "a": 0x41,    "b": 0x42,    "c": 0x43,    "d": 0x44,    "e": 0x45,
    "f": 0x46,    "g": 0x47,    "h": 0x48,    "i": 0x49,    "j": 0x4A,
    "k": 0x4B,    "l": 0x4C,    "m": 0x4D,    "n": 0x4E,    "o": 0x4F,
    "p": 0x50,    "q": 0x51,    "r": 0x52,    "s": 0x53,    "t": 0x54,
    "u": 0x55,    "v": 0x56,    "w": 0x57,    "x": 0x58,    "y": 0x59,  "z": 0x5A,

    # 입력 키 (특수문자)
    ";": 0xBA,    "=": 0xBB,    ",": 0xBC,    "-": 0xBD,    ".": 0xBE,
    "/": 0xBF,    "`": 0xC0,    "[": 0xDB,    "\\": 0xDC,    "]": 0xDD,
    "'": 0xDE,

    # 넘패드
    "num_lock": 0x90, "numpad_/": 0x6F, "numpad_*": 0x6A,
    "numpad_-": 0x6D, "numpad_+": 0x6B, "numpad_.": 0x6E,
    "numpad_7": 0x67, "numpad_8": 0x68, "numpad_9": 0x69,
    "numpad_4": 0x64, "numpad_5": 0x65, "numpad_6": 0x66,
    "numpad_1": 0x61, "numpad_2": 0x62, "numpad_3": 0x63,
    "numpad_0": 0x60,
}


# special letter
UPPER_SPECIAL = {
    "!": 1,    "@": 2,    "#": 3,    "$": 4,    "%": 5,    "^": 6,
    "&": 7,    "*": 8,    "(": 9,    ")": 0,    "_": "-",   "~": '`',    "|": '\\',
    "{": "[",   "}": "]",    ":": ";",    '"': "'", "?": "/", "<": ",", ">": "."
}


# move mouse specific location
def move_mouse(location):
    win32api.SetCursorPos(location)


# move mouse and left click
def click(location):
    # move mouse
    move_mouse(location)
    # left click
    l_click()


# move mouse and right click
def right_click(location):
    # move mouse
    move_mouse(location)
    # right click
    r_click()


# Double Click
def double_click(location):
    # move mouse
    move_mouse(location)
    # left click twice 
    l_click()
    l_click()


# key press only once
def key_press_once(key):
    # key push
    key_on(key)
    # key off
    key_off(key)



# push key
def key_on(key):
    # declare to approach KEYMAP
    global KEYMAP
    # convert to small letter
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # Extract key code
        key_code = KEYMAP[key.lower()]
        win32api.keybd_event(key_code, 0, 0x00, 0)
    except KeyError:
        # Error Message
        print(key + " is not an available key input.")
        sys.exit(1)


# key off
def key_off(key):
    # declare to approach KEYMAP
    global KEYMAP
    # conver to small letter
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # Extract key code
        key_code = KEYMAP[key.lower()]
        win32api.keybd_event(key_code, 0, 0x02, 0)
    except KeyError:
        #  Error Message
        print(key + " is not an available key input.")
        sys.exit(1)


# mouse left click
def l_click():
    # push left mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # push off  left mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# mouse right click
def r_click():
    # push right mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    # push off  right mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


#control_down
def control_down():
    key_on("control")
    key_on("down_arrow")
    key_off("control")
    key_off("down_arrow")

#control_up
def control_up():
    key_on("control")
    key_on("up_arrow")
    key_off("control")
    key_off("up_arrow")


#check str is digit
def is_digit(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False


# file
# 1.0 sec / c(blank)\n
f = open("test.txt", "r")

data = f.read()
data = data.replace("\n", "")
data = data.replace(" sec /", "")
melody = data.split(" ")
print(melody)

f.close()

# pa.moveTo(250, 250)
click((250,250))

# musescore start
key_press_once("n")

note = []
count = 0
for i in melody:
    if is_digit(i):
        speed = float(i)
        # print(speed)
        if speed >= 1.0:
            if speed >= 2:
                key_press_once("6")
            else:
                key_press_once("5")
            # print("Quarter note")
        elif speed < 1.0:
            # print("Quaver")
            key_press_once("4")
    else:
        note.append(i)
        key_press_once(i)
        if count == 0:
            control_down()
            count = 1

print(note)

# Extrack point that change octave
point = []
highpoint = []

for i in range(4,len(note)):
    if(note[i] != 'c'):
        if(note[i-4] != 'c'):
            if(note[i-1] == 'c'):
                point.append(i)

key_press_once("n")
# pa.moveTo(250, 250)
click((700,80))
# musescore start
key_press_once("n")

# IF i meet point, change low octave to high octave
for i in point:
    for j in range(0, len(note)):
        if(j >= i):
            control_up()
        key_on("right_arrow")
        key_off("right_arrow")
    key_press_once("n")
    # pa.moveTo(250, 250)
    click((700,80))
    # musescore start
    key_press_once("n")

for i in range(4,len(note)):
    if note[i-2] == 'g':
        if(note[i-1] == 'c'):
            highpoint.append(i)

key_press_once("n")
# pa.moveTo(250, 250)
click((700,80))
# musescore start
key_press_once("n")

#IF i meet highpoint, change high octave to low octave
for i in highpoint:
    for j in range(0, len(note)):
        if(j >= i):
            control_down()
        key_on("right_arrow")
        key_off("right_arrow")
    key_press_once("n")
    # pa.moveTo(250, 250)
    click((700,80))
    # musescore start
    key_press_once("n")
    
print(highpoint)
print(point)    

key_press_once("n")

#IF printer is 1, print screen appear
printer = int(input("Would you like to print it? (1.Yes/2.No)")) 
if (printer == 1) :
    click((500,160))
    key_on("control")
    key_on("p")
    key_off("control")
    key_off("p")
    key_on("alt")
    key_on("p")
    key_off("alt")
    key_off("p")
    

    
