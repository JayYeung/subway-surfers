import os
import h5py
from PIL import Image
import numpy as np
from tqdm import tqdm

path = "data"
image_data = []
labels = []

WIDTH = 3024
HEIGHT = 1490
SHRINK_FACTOR = 10

one_hot_encoding = {
    'left': 0, 
    'right': 1,
    'up': 2,
    'down': 3, 
    'nothing': 4   
}

for filename in tqdm(os.listdir(path), desc="Processing images"):
    if filename.endswith(".png"):
        file_path = os.path.join(path, filename)
        img = Image.open(file_path).resize((WIDTH // SHRINK_FACTOR, HEIGHT // SHRINK_FACTOR))
        img_array = np.array(img)
        image_data.append(img_array)
        encoding = [0] * 5
        encoding[one_hot_encoding[filename.split('_')[-1].split('.')[0]]] = 1
        labels.append(encoding)

image_data = np.array(image_data)
labels = np.array(labels)

with h5py.File('image_data_with_labels.h5', 'w') as hf:
    hf.create_dataset('image_data', data=image_data)
    hf.create_dataset('labels', data=labels)

print("HDF5 file created with image data and labels.")
print(f"Image data shape: {image_data.shape}")
print(f"Labels shape: {labels.shape}")