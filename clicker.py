import pyautogui
import time
import os


MINUTES_TO_PAUSE = 10


def convert_to_preferred_format(timestamp):
    # sec = timestamp % (24 * 3600)
    # hour = sec // 3600
    # sec %= 3600
    # min = sec // 60
    # sec %= 60
    # # return "%02d:%02d:%02d" % (hour, min, sec)
    # return hour, min, sec
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
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        print('\nMove mouse to close window button...')
        time.sleep(4)
        x_close, y_close = pyautogui.position()
        print("\n\nPosition acquired! Auto clicking will run for %02d:%02d... \nPress Ctrl-C to quit.\n" % (max_hours, max_mins))

        wait_time = .0
        now = time.time()
        while True:
            old_now = now
            now = time.time()
            wait_time += now - old_now
            running_time = now - start_time
            running_hours, running_mins, running_secs = convert_to_preferred_format(running_time)
            if running_hours >= max_hours and running_mins >= max_mins:
                print('\nMax running time reached. Stopping...')
                os.system('say "Max running time reached. Stopping..."')
                pyautogui.click(x_close, y_close, clicks=1, button="left")  # click 'close window' button
                exit(0)
            print(f'\rRunning time: %02d:%02d:%02d' % (running_hours, running_mins, running_secs), end=' ')
            _, wait_mins, _ = convert_to_preferred_format(wait_time)
            if wait_mins >= MINUTES_TO_PAUSE:
                wait_time = .0
                pyautogui.click(x, y - 60, clicks=1, button="left")  # click on window to bring it in first plane
                pyautogui.click(x, y, clicks=1, button="left")  # click on selected position
            # time.sleep(50)

    except KeyboardInterrupt:
        print('\nTerminated.')


if __name__ == "__main__":
    main()
