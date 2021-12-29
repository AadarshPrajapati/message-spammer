import pyautogui as df
import time

time.sleep(3)
# print(df.position())
# Point(x=555, y=698)
df.moveTo(555,698,duration=0)
df.click(555,698)

file = open('spam.txt', 'r')

while 1:
    # read by character
    char = file.read(1)
    if not char:
        break
    df.typewrite(char)
    df.press('enter')
file.close()
