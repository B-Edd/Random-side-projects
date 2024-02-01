import pyautogui
import time
from PIL import ImageGrab

def get_pixel_color(x, y):
    # Grab a screenshot
    screenshot = ImageGrab.grab()
    # Get pixel color at (x, y)
    color = screenshot.getpixel((x, y))
    return color


def moveclick(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

time.sleep(3)
lr = 0
for i in range(203, 250):
    if lr == 0:
        moveclick(1136, 865)  # right
        pyautogui.typewrite(str(i))
        pyautogui.press('enter')
        lr = 1
        time.sleep(2)
    else:
        moveclick(444, 855)  # left
        pyautogui.typewrite(str(i))
        pyautogui.press('enter')
        lr = 0
        time.sleep(2)

