import pyautogui
import time

while True:
  try:
    img = pyautogui.locateOnScreen('activamap.JPG', confidence=0.8, grayscale = True)
    print('Found it!')
    print(img)
    while True:
      try:
        img = pyautogui.locateOnScreen('activamap.JPG', confidence=0.8, grayscale = True)
        print('Found it!')
        print(img)
        pyautogui.click(x=882, y=752, button= 'left')
        time.sleep(2)
        pyautogui.write('840-8E3-95-BBCBE')
        time.sleep(2)
        pyautogui.press('enter')
        break
      except:
        pass
    time.sleep(5)
    time.sleep(2)
    break
  except:
    pass
time.sleep(5)
while True:
  try:
    img = pyautogui.locateOnScreen('activamap.JPG', confidence=0.8, grayscale = True)
    print('Found it!')
    print(img)
    pyautogui.click(x=882, y=752, button= 'left')
    time.sleep(2)
    pyautogui.write('840-8E3-95-BBCBE')
    time.sleep(2)
    pyautogui.press('enter')
    break
  except:
    pass
time.sleep(5)
while True:
  try:
    img = pyautogui.locateOnScreen('activamap.JPG', confidence=0.8, grayscale = True)
    print('Found it!')
    print(img)
    pyautogui.click(x=882, y=752, button= 'left')
    time.sleep(2)
    pyautogui.write('840-8E3-95-BBCBE')
    time.sleep(2)
    pyautogui.press('enter')
    break
  except:
    pass
time.sleep(5)
