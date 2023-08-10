import pyautogui
import time
import os
import random


def convert_to_preferred_format(timestamp):
    hours, rem = divmod(timestamp, 3600)
    minutes, seconds = divmod(rem, 60)
    return hours, minutes, seconds


def main():
    try:
        start_time = time.time()
        print("Enter running time...")
        max_hours = int(input("Hours:"))
        max_mins = int(input("Minutes:"))
        print('\nMove mouse to autoclick position...')
        time.sleep(4)
        x, y = pyautogui.position()
        print("\nPosition acquired!")
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
        print('\nMove mouse to close window button...')
        time.sleep(4)
        x_close, y_close = pyautogui.position()
        print("\n\nPosition acquired! Auto clicking will run for %02d:%02d... \nPress Ctrl-C to quit.\n" % (max_hours, max_mins))

        waiting_time = .0
        minutes_to_wait = random.randint(1, 6)
        now = time.time()
        while True:
            old_now = now
            now = time.time()
            waiting_time += now - old_now
            running_time = now - start_time
            running_hours, running_minutes, running_seconds = convert_to_preferred_format(running_time)
            if running_hours >= max_hours and running_minutes >= max_mins:
                print('\nMax running time reached. Stopping...')
                os.system('say "Max running time reached. Stopping..."')
                pyautogui.click(x_close, y_close, clicks=1, button="left")  # click 'close window' button
                exit(0)
            print(f'\rRunning time: %02d:%02d:%02d' % (running_hours, running_minutes, running_seconds), end=' ')
            _, wait_minutes, _ = convert_to_preferred_format(waiting_time)
            if wait_minutes >= minutes_to_wait:
                waiting_time = .0
                minutes_to_wait = random.randint(1, 6)
                x_last, y_last = pyautogui.position()  # get current mouse position
                pyautogui.click(x, y - 60, clicks=1, button="left")  # click on window to bring it in first plane
                pyautogui.click(x, y, clicks=1, button="left")  # click on selected position
                pyautogui.moveTo(x_last, y_last)  # move mouse to last position
            time.sleep(5)

    except KeyboardInterrupt:
        print('\nTerminated.')


if __name__ == "__main__":
    main()
