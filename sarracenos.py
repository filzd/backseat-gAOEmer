import os
import pyautogui

# makes sure mkt is selected
pyautogui.press('t')
i = 0

bao = ['shirt', 'dingding']

# any  'infinite' condition
while bao:
    
# the abuse itself
    while i < 10:
        pyautogui.hotkey('shift', 'p')
        pyautogui.hotkey('shift', ';')
        pyautogui.hotkey('shift','o')
        pyautogui.hotkey('shift','l')
        pyautogui.hotkey('shift','i')
        pyautogui.hotkey('shift','k')
        i += 1
    bao.pop()

