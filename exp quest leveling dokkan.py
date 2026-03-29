import time
import pyautogui
import sys

try:
    while True:

        print("Playing Dokkan")
        time.sleep(0.5)

        #Level Up
        pyautogui.click(button='left',clicks=3,interval=0.25,x=170,y=865)
        time.sleep(1)

        # Cancel Friend Request
        pyautogui.click(button='left',clicks=1,interval=0.25,x=170,y=865)
        time.sleep(1)

        # Push Attempt Again
        pyautogui.click(button='left',clicks=1,interval=0.25,x=183,y=1194)
        time.sleep(1)

        # Push Confirm Again
        pyautogui.click(button='left',clicks=1,interval=0.25,x=442,y=833)
        time.sleep(2.5)

        # Push Start
        pyautogui.click(button='left',clicks=1,interval=0.25,x=517,y=1212)
        time.sleep(1)
       

        buff = 50
        print("50s buffer. PLease CTRL-C here if you need to escape. \n")
        for i in range(0, buff):
            print(".", end = " ")
            time.sleep(1)
        print("\n")

except KeyboardInterrupt:
    print('\nExiting. \n')