import pyautogui
import os
import cv2

def takeScreenshot():
    # makes sure 'economy mode' is active
    pyautogui.hotkey("ctrl", "r")
    
    # rough location of sell and buy prices
    MktAbuse = pyautogui.screenshot(region=(2048, 1080, 500, 200))
    MktAbuse.save(r'C:\Users\idk\backseat-gAOEmer\Screenshots\MktAbuse.jpg')
    
takeScreenshot()