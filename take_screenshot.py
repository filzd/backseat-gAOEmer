import pyautogui
import os

def takeScreenshot():
    screenshot_folder = r'C:\Users'
    screenshot_name = 'screenshot.png'
    screenshot_path = os.path.join(screenshot_folder, screenshot_name)
    
    pyautogui.alert('This is an alert box.')
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    folder_path = os.path.join(desktop_path, "New folder")
    
    image_path = os.path.join(folder_path, "image.png")
    saracenIconLocation = pyautogui.locateOnScreen('image_path')
    return saracenIconLocation


print(takeScreenshot())