from selenium import webdriver
import datetime
from pynput import keyboard
import os
import threading
import time

driver = webdriver.Chrome()
URL = "https://superteamxx.github.io/Subway-Surfers/"
path = "data"

driver.execute_script(f"window.open('{URL}', '_blank');")
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])

RUN_NUMBER = 0
round_start_time = datetime.datetime.now()
last_action_time = datetime.datetime.now()
screenshots_taken = []
lock = threading.Lock()

def take_screenshot(action='nothing'):
    global RUN_NUMBER, round_start_time, screenshots_taken
    time_elapsed = (datetime.datetime.now() - round_start_time).seconds
    naming_convention = f'{RUN_NUMBER}_{time_elapsed}_{action}'
    screenshot_filename = f'{path}/{naming_convention}.png'
    driver.save_screenshot(screenshot_filename)
    screenshots_taken.append(screenshot_filename)
    print(f"Screenshot saved as {naming_convention}.png")

def check_inactivity():
    global last_action_time
    while True:
        with lock:
            time_since_last_action = (datetime.datetime.now() - last_action_time).seconds
            if time_since_last_action >= 1:
                take_screenshot()
        time.sleep(0.5)

def on_press(key):
    global round_start_time, last_action_time, lock, screenshots_taken, RUN_NUMBER
    with lock:
        last_action_time = datetime.datetime.now()

        if key in [keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right]:
            action = str(key).split('.')[1]
            take_screenshot(action=action)

        elif key == keyboard.Key.esc:
            driver.quit()
            return False

        elif key == keyboard.Key.space:
            # delete mistakes that caused you to die. 
            for _ in range(3):
                if screenshots_taken:
                    last_screenshot = screenshots_taken.pop()
                    if os.path.exists(last_screenshot):
                        os.remove(last_screenshot)
                        print(f"Deleted {last_screenshot}")

            RUN_NUMBER += 1
            round_start_time = datetime.datetime.now()
            screenshots_taken = []

inactivity_thread = threading.Thread(target=check_inactivity)
inactivity_thread.daemon = True
inactivity_thread.start()

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

driver.quit()
