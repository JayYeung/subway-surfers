from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput import keyboard
from time import sleep
import pyautogui

URL = "https://superteamxx.github.io/Subway-Surfers/"

TOP_X, TOP_Y = 500, 300
WEIRD_OFFSET = 40
X, Y = TOP_X, TOP_Y + 170 - WEIRD_OFFSET
WIDTH, HEIGHT = 570, 310
BOTTOM_X, BOTTOM_Y = X + WIDTH, Y + HEIGHT 

ACTIONS = ['left', 'right', 'up', 'down', 'nothing']
REVERSE_KEYBOARD = [keyboard.Key.left, keyboard.Key.right, keyboard.Key.up, keyboard.Key.down, None]
REVERSE_ENCODING = [Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_UP, Keys.ARROW_DOWN, '']
ACTION_TO_INDEX = {action: i for i, action in enumerate(ACTIONS)} 

def start():
    driver = webdriver.Chrome()

    driver.set_window_position(TOP_X, TOP_Y) 
    driver.set_window_size(570, 450) 

    driver.execute_script(f"window.open('{URL}', '_blank');")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
    sleep(10) # loading
    print('Starting up...')
    pyautogui.moveTo(TOP_X + 220, TOP_Y + 340 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 280, TOP_Y + 340 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 290, TOP_Y + 450 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 260, TOP_Y + 350 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 280, TOP_Y + 400 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 180, TOP_Y + 190 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 220, TOP_Y + 250 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 220, TOP_Y + 280 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    pyautogui.moveTo(TOP_X + 200, TOP_Y + 200 - WEIRD_OFFSET)
    pyautogui.click()
    sleep(0.1)
    
    return driver


def extract_info(name):
    run_number, time_elapsed = name.split('_')
    time_elapsed = float(time_elapsed.rstrip('.png'))
    return run_number, time_elapsed

def get_time_elapsed(name):
    return extract_info(name)[1]

def get_action(name):
    return extract_info(name)[0]

