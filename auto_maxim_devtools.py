import pyautogui
import time

# pyautogui.moveTo(500, 30)

def maxim_devtools():
    time.sleep(1)

    # Move to the location and double-click
    pyautogui.doubleClick(x=500, y=30)

    # Press F12
    pyautogui.press('f12')