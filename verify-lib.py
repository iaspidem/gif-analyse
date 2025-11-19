from PIL import Image
import imageio

def read_input():

    return

def pillow_fn(img):
    duration = 0

    while True:
        try:
            frame_duration = img.info['duration']
            duration += frame_duration
            img.seek(img.tell() + 1)
        except EOFError:
            break

    return duration

def imageio_fn(gif):
    duration = 0

    for frame in gif:
        duration += gif.get_meta_data(index=frame)["duration"]

    return duration