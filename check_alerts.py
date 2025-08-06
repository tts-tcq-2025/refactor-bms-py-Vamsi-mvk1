import sys
from time import sleep

def blink_alert(duration=2):
    total_flashes = duration * 2
    for i in range(total_flashes):
        state = '\r* ' if i % 2 == 0 else '\r *'
        print(state, end='')
        sys.stdout.flush()
        sleep(1)
