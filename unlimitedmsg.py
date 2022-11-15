import pyautogui
import time
time.sleep(4)
count=0
while count<=200:
    pyautogui.typewrite("hi  ZA" +str(count))
    pyautogui.press("enter")
    count=count+1
