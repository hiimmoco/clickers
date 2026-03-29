import time
import pyautogui
import sys


try:
    while True:

        print("Playing All Stars")
        time.sleep(0.5)


        # Accept Dragon Stone
        pyautogui.click(button='left',clicks=1,interval=0.5,x=306,y=902)
        time.sleep(1)

        # OK
        pyautogui.click(button='left',clicks=1,interval=0.5,x=300,y=1198)
        time.sleep(1)

        # Cancel Friend Request and Go Next
        pyautogui.click(button='left',clicks=3,interval=0.5,x=225,y=865)
        time.sleep(1)

        # Click Level
        pyautogui.click(button='left',clicks=4,interval=0.5,x=310,y=912)
        time.sleep(2.5)

        # Push Start
        pyautogui.click(button='left',clicks=1,interval=0.5,x=517,y=1212)
        time.sleep(1)
       

        buff = 105
        print("105s buffer. Please CTRL-C here if you need to escape. \n")
        for i in range(0, buff):
            print(".", end = "")
            time.sleep(1)
        print("\n")



except KeyboardInterrupt:
    print('\nExiting. \n')
except pyautogui.FailSafeException:
    print('\nExiting. \n')