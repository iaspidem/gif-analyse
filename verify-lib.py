import os
from PIL import Image
import imageio

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

def verify_fn(dir):
    for path, folders, files in os.walk(dir):
        # Open file
        for filename in files:
            print(f"{filename}")
            #print(f"Filepath: {filepath}")

        for folder_name in folders:
            print(f"Content of '{folder_name}'")
            # List content from folder
            print(os.listdir(f"{path}/{folder_name}"))
            print()
    #break   

# Assign directory
dir = r"data"

verify_fn(dir)