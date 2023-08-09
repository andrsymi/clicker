import pyautogui
import time


def main():
    # print('Press Ctrl-C to quit.')
    #
    # try:
    #     while True:
    #         x, y = pyautogui.position()
    #         # print(x, y, flush=True)
    #         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #         print(positionStr, end='')
    #         print('\b' * len(positionStr), end='', flush=True)
    #
    # except KeyboardInterrupt:
    #     print('\nDone.')

    for i in range(1, 11):
        print('\r', "kalimera", i, end='')
        time.sleep(1)
    # Add print after loop for a new line, when finishing
    print()


if __name__ == "__main__":
    main()
