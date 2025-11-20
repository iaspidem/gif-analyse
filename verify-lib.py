import os
from PIL import Image
import imageio

def pillow_fn(filepath):
    img = Image.open(filepath)
    duration = 0

    while True:
        try:
            frame_duration = img.info['duration']
            duration += frame_duration
            img.seek(img.tell() + 1)
        except EOFError:
            break

    return duration

def imageio_fn(filepath):
    gif = imageio.get_reader(filepath)
    duration = 0
    frame_counter = 0

    for frame in gif:
        frame_counter +=1
        duration += gif.get_meta_data(index=frame)["duration"]
        fps = frame_counter / (duration / 1000)

    return duration, frame_counter, fps

def verify_fn(dir):
    folder_path = r"data/"

    for path, folders, files in os.walk(dir):
        # Open file
        for filename in files:
            print("===============================================")
            print(f"{filename}")
            filepath = str(folder_path) + filename
            #print(f"Filepath: {filepath}")

            dur1 = pillow_fn(filepath)
            dur2, frame_counter, fps = imageio_fn(filepath)
            if dur1 == dur2:
                print(f"Duration: {dur1} ms")
                print(f"Total number of frames: {frame_counter} frames")
                print(f"Frames per second: {fps} fps")
                print("===============================================")
                print()
            else:
                print(f"ERROR: {dur1}ms vs {dur2}ms")
                return

        for folder_name in folders:
            print(f"Content of '{folder_name}'")
            # List content from folder
            print(os.listdir(f"{path}/{folder_name}"))
            print()
            folder_path = str(f"{path}/{folder_name}") + "/"
    
    print("Processing complete.")

# Assign directory
dir = r"data"

verify_fn(dir)