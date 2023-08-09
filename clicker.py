import pyautogui
import time
import os
from playsound import playsound


def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    # return "%02d:%02d:%02d" % (hour, min, sec)
    return hour, min, sec


def main():
    try:
        start = time.time()
        print("Enter running time...")
        max_hours = int(input("Hours:"))
        max_mins = int(input("Minutes:"))
        print('\nMove mouse to autoclick position...')
        time.sleep(4)
        x, y = pyautogui.position()
        print("\nPosition acquired!")
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        print('\nMove mouse to close window button...')
        time.sleep(4)
        x_close, y_close = pyautogui.position()
        print("\n\nPosition acquired! Auto clicking will run for %02d:%02d... \nPress Ctrl-C to quit.\n" % (max_hours, max_mins))

        while True:
            now = time.time() - start
            hours, mins, secs = convert_to_preferred_format(now)
            if hours >= max_hours and mins >= max_mins:
                print('\nMax running time reached. Stopping...')
                playsound('bell.mp3')
                pyautogui.click(x_close, y_close, clicks=1, button="left")  # click 'close window' button
                exit(0)
            print(f'\rRunning time: %02d:%02d:%02d' % (hours, mins, secs), end=' ')
            pyautogui.click(x, y - 60, clicks=1, button="left")  # click on window to bring it in first plane
            pyautogui.click(x, y, clicks=1, button="left")  # click on selected position
            time.sleep(50)

    except KeyboardInterrupt:
        print('\nTerminated.')


if __name__ == "__main__":
    main()
