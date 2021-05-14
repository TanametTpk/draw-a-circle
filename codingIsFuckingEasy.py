import os
import time

size = os.get_terminal_size()
weight = size.columns
height = size.lines

r = height / 5
h = weight / 2
k = height / 2

for y in range(height):
    for x in range(weight):
        if (x - h)**2 + (y - k)**2 > r**2:
            print(chr(219), end="")
        else:
            print(" ", end="")
    time.sleep(0.01)
    print("")