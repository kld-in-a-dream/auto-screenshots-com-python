import pyautogui
import datetime
import time

while True:
    now = datetime.datetime.now()
    now_str = now.strftime('%d-%H-%M-%S')
    starttime = time.time()
    scr1 = pyautogui.screenshot()
    scr1.save('{}.png'.format(now_str))
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))