import pyautogui
import os
import cv2

def takeScreenshot():
    screenshot_folder = r'C:\Users\idk\backseat-gAOEmer\Screenshots'
    screenshot_name = 'screenshot.png'
    screenshot_path = os.path.join(screenshot_folder, screenshot_name)
    screenshot = pyautogui.screenshot()

    # Save the screenshot to a file
    screenshot.save(screenshot_path)

    # image we are looking for 
    folder_path = r'C:\Users\Desktop\image_folder'
    #image_path = os.path.join(folder_path, "image.png")
    
    image1 = cv2.imread(os.path.join(folder_path, 'image.png'))
    image2 = cv2.imread(os.path.join(screenshot_path, 'screenshot.png'))
    
    result = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)
    
    if cv2.minMaxLoc(result)[1] > 0.9:
        print("Images match")
    else:
        print("Images do not match")


takeScreenshot()