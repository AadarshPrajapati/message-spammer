import pyautogui as df
import time

time.sleep(3)
# Point(x=1085, y=707)
df.moveTo(1085,707,duration=0)
df.click(1085,707)

with open('spam.txt', 'r') as file:

    for line in file:
        for word in line.split():
            df.typewrite(word)
            df.press('enter')
file.close()

