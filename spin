#spinny visual experiment
'''
goal:
print a line that appear to go clockwise
''' 

import sys
import time

print ("processing...",)
syms = ['\\', '|', '/', '-']
bs = '\b'

for _ in range(10):  <--- How many cycles
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(.1) <------speed

print ('yay')
