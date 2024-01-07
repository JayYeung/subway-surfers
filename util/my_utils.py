from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://superteamxx.github.io/Subway-Surfers/"

TOP_X, TOP_Y = 500, 300
WEIRD_OFFSET = 30
X, Y = TOP_X, TOP_Y + 170 - WEIRD_OFFSET
WIDTH, HEIGHT = 570, 310
BOTTOM_X, BOTTOM_Y = X + WIDTH, Y + HEIGHT 

ACTIONS = ['left', 'right', 'up', 'down', 'nothing']
REVERSE_ENCODING = [Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_UP, Keys.ARROW_DOWN, '']

def start():
    driver = webdriver.Chrome()

    driver.set_window_position(TOP_X, TOP_Y) 
    driver.set_window_size(570, 450) 

    driver.execute_script(f"window.open('{URL}', '_blank');")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
    return driver

def extract_info(name):
    run_number, time_elapsed, action = name.split('_')
    action = action.split('.')[0]
    return run_number, time_elapsed, action

def get_time_elapsed(name):
    return int(extract_info(name)[1])

def get_action(name):
    return extract_info(name)[2]
