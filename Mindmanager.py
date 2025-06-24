import pyautogui
import time

pyautogui.click(x=1848, y=123, button= 'right')
pyautogui.press('down', presses= 3, interval= 1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=1348, y=698)
time.sleep(1)
pyautogui.click(x=1453, y=356, button= 'right')
time.sleep(1)
pyautogui.press('down', presses= 3, interval= 1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('pepito')
pyautogui.press('enter')