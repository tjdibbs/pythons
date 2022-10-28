import math
from random import random
import pyautogui
import time

time.sleep(4)
count = 0

def messages(i: int):
  dummies = ["I Love you marble.", "Sweetheart celeb", "God bless you", "Please take care of urself", "Stay happy", "Mama"]
  index = math.floor(random() * 7)
  if(index > len(dummies) - 1):
    return dummies[index - 2] + " " + str(i)
  else:
    return dummies[index] + " " + str(i)

while count <= 200:
  pyautogui.write(messages(count))
  pyautogui.press("enter")
  count += 1
