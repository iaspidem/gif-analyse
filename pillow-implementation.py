# import pillow
from PIL import Image

img = Image.open("data/Steam-SunsetCruise/Artwork_Featured.gif")

duration = 0

while True:
    try:
        frame_duration = img.info['duration']
        duration += frame_duration
        img.seek(img.tell() + 1)
    except EOFError:
        break

print(f"Total duration: {duration} ms")