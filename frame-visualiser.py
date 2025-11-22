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

img.seek(0)
img.save("output/img_begin.png")
img.seek(img.n_frames - 1)
img.save("output/img_end.png")

#frames = []
#frames.append(img.seek(0))
#frames.append(img.seek(img.n_frames - 1))

#frames[0].save("visualiser-output.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)