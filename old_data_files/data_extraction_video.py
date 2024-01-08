from selenium import webdriver
import cv2
import numpy as np
from mss import mss
import time
from datetime import datetime
from util.my_utils import start, X, Y, BOTTOM_X, BOTTOM_Y, WIDTH, HEIGHT, ACTIONS, REVERSE_KEYBOARD
from pynput import keyboard
import os
import csv

driver = start()
file_path = 'data'
RUN_NUMBER = 2
recording = False  
running = True
start_time = None

if not os.path.exists(f"{file_path}/_actions.csv"):
    with open(f"{file_path}/_actions.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Run Number", "Action", "Time Elapsed"])

def on_press(key):
    global RUN_NUMBER, recording, start_time, running

    if key == keyboard.Key.space:
        if not recording:
            print('STARTING THE RECORDING')
            RUN_NUMBER += 1
            start_time = time.time()
            recording = True
        else:
            print('STOPPING THE RECORDING')
            recording = False
    
    elif key == keyboard.Key.esc:
        print('STOPPING THE PROGRAM, was on run', RUN_NUMBER)
        driver.quit()
        recording = False
        running = False
        return False
    
    elif recording:
        if key in REVERSE_KEYBOARD[:-1]:  # Exclude 'nothing' action
            action = ACTIONS[REVERSE_KEYBOARD.index(key)]
            time_elapsed = time.time() - start_time
            with open(f"{file_path}/_actions.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([RUN_NUMBER, action, time_elapsed])

listener = keyboard.Listener(on_press=on_press)
listener.start()

with mss() as sct:
    monitor = {"top": Y, "left": X, "width": WIDTH, "height": HEIGHT}

    while running:
        if recording:
            sct_img = sct.grab(monitor)
            frame = np.array(sct_img)
            cv2.imwrite(f"{file_path}/{RUN_NUMBER}_{time.time()-start_time}.png", frame)

        if not recording and start_time is not None:
            if time.time() - start_time > 1:
                start_time = None  

listener.stop()
