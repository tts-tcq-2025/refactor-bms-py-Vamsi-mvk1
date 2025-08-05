import sys
from time import sleep

def blink_alert(duration=6):
    states = ['\r* ', '\r *']
    for _ in range(duration):
        for state in states:
            print(state, end='')
            sys.stdout.flush()
            sleep(1)
