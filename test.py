import keyboard
import time
string = ''
while True:
    if keyboard.is_pressed("esc"):
        string += 'h'
   
    time.sleep(1)
    if string=="hhh":
        break