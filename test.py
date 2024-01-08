from util.my_utils import start, X, Y, BOTTOM_X, BOTTOM_Y

from datetime import datetime
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui

driver = webdriver.Chrome()

URL = "https://superteamxx.github.io/Subway-Surfers/"

driver.set_window_position(0, 0) 
driver.set_window_size(570, 450) 

X, Y = 0, 170
BOTTOM_X, BOTTOM_Y = 570, 480

driver.execute_script(f"window.open('{URL}', '_blank');")
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.get(URL)

start = datetime.now()

while True: 
    img = ImageGrab.grab(bbox=(X, Y, BOTTOM_X, BOTTOM_Y))
    print('Screenshot latency (seconds):', (datetime.now() - start).total_seconds())
    img.save('current_frame.png')

    start = datetime.now()
    