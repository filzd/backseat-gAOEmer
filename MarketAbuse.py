import pyautogui

def sara_mkt_abuse():
    
    # makes sure mkt is selected
    pyautogui.press('t')

    number_of_abuses = 0
    
    # how many times we want to cycle the commands
    while number_of_abuses < 10:
        # sell - buy stone
        pyautogui.hotkey('shift', 'p')
        pyautogui.hotkey('shift', ';')
            
        # sell - buy food
        pyautogui.hotkey('shift','o')
        pyautogui.hotkey('shift','l')
            
        # sell - buy wood
        pyautogui.hotkey('shift','i')
        pyautogui.hotkey('shift','k')
        
        number_of_abuses += 1
