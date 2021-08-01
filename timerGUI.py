import PySimpleGUI as sg
import time
import sys
import os

"""A GUI-based pomodoro timer, allowing you to choose the lenth of
 the work and pause periods"""


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

def main():
    sg.theme('DarkRed1')

    layout = [  [sg.Text('Welcome to the pomodoro timer! Focus on your work...')],
                [sg.Text('                              ')],
                [sg.Text('How many minutes do you want to work for?: '), sg.InputText(size=(3,1), key='-IN-')],
                [sg.Text('How many minutes break?: '), sg.InputText(size=(3,1), key='-CHAR-')],
                [sg.Text('How many sessions?: '), sg.InputText(size=(3,1), key='-SESS-')],
                [sg.Button('Go!')],
                [sg.Text('                              ')],
                # [sg.Text('Latest:'), sg.Text(size=(15,1), key='-OUT-')],
                # [sg.Text('                              ')],
                [sg.Button('Close Window')]
                ]

    window = sg.Window("Gillian's 'pomodoro' timer", layout,size=(400, 400))

    while True:
        event, values = window.read()
        # End program if user closes window
        if event == "Close Window" or event == sg.WIN_CLOSED:
            break
        if event == 'Go!':
            interval = int(values['-IN-'])
            break_duration = int(values['-CHAR-'])
            total_duration = int(values['-SESS-'])

            session_count = 0
            """Voice announcement of each change from work to break and back"""

            while session_count < total_duration:

                os.system('say "time to get to work!"')
                count = countdown(interval)
                window['-OUT-'].update(count)
                os.system('say "time for a break!"')
                # print('\nBreak time!')
                rest = countdown(break_duration)
                window['-OUT-'].update(rest)
                # countdown(break_duration)
                session_count += 1


            os.system('say "Well done! You are getting better every day."')
            # print('\nEnd of Session!')


            # pomo = countdown(interval)

    window.close()

if __name__ == '__main__':
    main()
