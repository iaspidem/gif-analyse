import os
import math
import imageio

def imageio_fn(filepath):
    gif = imageio.get_reader(filepath)
    duration = 0
    frame_count = 0

    for frame in gif:
        frame_count += 1
        duration += gif.get_meta_data(index=frame)["duration"]

    fps = frame_count * 1000 / duration

    return duration, frame_count, fps

def verify_fn(dir):
    folder_path = r"data/"

    for path, folders, files in os.walk(dir):
        # Open file
        for filename in files:
            print("===============================================")
            print(f"{filename}\n")
            filepath = str(folder_path) + filename
            #print(f"Filepath: {filepath}")

            file_size = os.path.getsize(filepath)
            print(f"Raw file size: {file_size} bytes")
            print(f"File size: {int(round(file_size / 1024, 0))} KB ({round(file_size / pow(1024, 2), 2)} MB)")

            duration, frame_count, fps = imageio_fn(filepath)

            print(f"Duration: {duration} ms")
            print(f"Total number of frames: {frame_count} frames")
            print(f"Frames per second: {fps} fps")
            print("===============================================")
            print()

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