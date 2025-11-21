import os
import math
import imageio
from PIL import Image

filepath = "data/delorean-retroloop.gif"

file_size = os.path.getsize(filepath)
print(f"Raw file size: {file_size} bytes")
print(f"File size: {int(round(file_size / 1024, 0))} KB ({round(file_size / pow(1024, 2), 2)} MB)")

img = Image.open(filepath)
print("Number of frames (n_frames): " + str(img.n_frames))