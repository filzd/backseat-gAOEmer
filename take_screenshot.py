import pyautogui

def takeScreenshot():
    entire_map = pyautogui.screenshot()
    entire_map.save('map.png')
    