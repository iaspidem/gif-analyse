import imageio
from PIL import Image

filepath = "data/delorean-retroloop.gif"

# check number of frames
gif = imageio.get_reader(filepath)
frame_counter = 0

for frame in gif:
    frame_counter +=1

print(f"Number of frames (imageio): {frame_counter}")

img = Image.open(filepath)
print("Number of frames (n_frames): " + str(img.n_frames))