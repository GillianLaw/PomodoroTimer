import time
import sys
# from playsound import playsound
import os

"""A basic pomodoro timer, allowing you to choose the lenth of
 the work and pause periods"""

interval = int(input('How many minutes do you want to work for?: '))
break_duration = int(input('How many minutes break?: '))
total_duration = int(input('How many sessions?: '))

# interval = 25
def countdown(interval):
    for i in range(interval,0,-1):
        for j in range(59,0,-1):

            if i <= 1:
                sys.stdout.write \
                (f'\rYou have just {j} seconds to go              ')

            else:
                sys.stdout.write \
                (f'\rYou have {i-1} minutes and {j} seconds to go ')
            sys.stdout.flush()
            time.sleep(1)


if __name__ == "__main__":
    session_count = 0
    """Voice announcement of each change from work to break and back"""
    
    while session_count < total_duration:

        os.system('say "time to get to work!"')
        countdown(interval)
        os.system('say "time for a break!"')
        print('\nBreak time!')
        countdown(break_duration)
        session_count += 1
        print('\nsession number: ',session_count)
    os.system('say "Well done! You are getting better every day."')
    print('\nEnd of Session!')
