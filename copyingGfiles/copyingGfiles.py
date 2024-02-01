import pyautogui
import time

time.sleep(2)


def moveclick(x, y, t=3):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(t)


def removetab():
    time.sleep(2)
    pyautogui.moveTo(131, 0)
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(300, 207)
    pyautogui.click()

for i in range(24):
    time.sleep(3)
    moveclick(73, 168, t=1)  # file

    moveclick(91, 265, t=1)  # make a copy
    moveclick(513, 270, t=1)  # make a copy
    # rmoeve "copy of"
    keys_to_press = ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']
    for key in keys_to_press:
        pyautogui.press(key)
    for i in range(8):
        pyautogui.press('backspace')
    moveclick(656, 546)  # folder
    moveclick(661, 280, t=1)  # all locations
    moveclick(988, 325)  # mydrive
    moveclick(988, 325)  # gr. 9
    moveclick(988, 520)  # science
    moveclick(914, 325)  # select teacher lesson folder
    moveclick(810, 636)  # make a copy
    time.sleep(6)
    moveclick(848, 135)
    removetab()
    time.sleep(2)
    moveclick(848, 135)
    removetab()
    time.sleep(1)
