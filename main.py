import pyautogui
import math
import time

pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0

def percent2Angle(percent):
    # +5 for vole.wtf to recognition circle
    return (360 + 5) / 100 * percent

def getTargetPosition(rawAngle):
    angle = math.radians(rawAngle)
    x = h + r * math.cos(angle)
    y = k + r * math.sin(angle)
    return x, y

# set radius
r = 250

# get mouse position
h, k = pyautogui.position()
x, y = getTargetPosition(0)
pyautogui.moveTo(x, y, _pause=False)

# hold left
pyautogui.mouseDown()

# draw circle
RESULOTION = 90000
for i in range(RESULOTION):
    angleRaw = percent2Angle(i / (RESULOTION / 100))
    angle = math.radians(angleRaw)
    x = h + r * math.cos(angle)
    y = k + r * math.sin(angle)
    pyautogui.moveTo(x, y, _pause=False)

# release left
time.sleep(1)
pyautogui.mouseUp()