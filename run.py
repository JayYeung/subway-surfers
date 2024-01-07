from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import numpy as np
import tensorflow as tf
from datetime import datetime
from PIL import ImageGrab
from util.my_utils import start, X, Y, BOTTOM_X, BOTTOM_Y, ACTIONS, REVERSE_ENCODING


model = tf.keras.models.load_model(r'computer_vision/model.keras', compile=False)

driver = start()

latency = datetime.now()

# sleep(60)

try:
    actions = ActionChains(driver)

    while True:
        img = ImageGrab.grab(bbox=(X, Y, BOTTOM_X, BOTTOM_Y)).convert('RGB')
        current_frame = np.array([np.array(img)])
        prediction = np.argmax(model.predict(current_frame, verbose=0))
        print('Prediction:', ACTIONS[prediction])
        # print('Latency (seconds):', (datetime.now() - latency).total_seconds())
        latency = datetime.now()
        actions.send_keys(REVERSE_ENCODING[prediction]).perform()
except KeyboardInterrupt:
    print("Stopped by user")

finally:
    driver.quit()


driver.quit()
