import sys
from time import sleep
def blink_alert(duration=6, step_duration=1):
    # step_duration = how long each half-blink lasts (in seconds)
    total_steps = int(duration / step_duration)
    states = ['\r* ', '\r *']
    
    for i in range(total_steps):
        print(states[i % 2], end='')
        sys.stdout.flush()
        sleep(step_duration)





# def blink_alert(duration=2):
#     total_flashes = duration * 2
#     for i in range(total_flashes):
#         state = '\r* ' if i % 2 == 0 else '\r *'
#         print(state, end='')
#         sys.stdout.flush()
#         sleep(1)
