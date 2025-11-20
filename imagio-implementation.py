#import module
import imageio

gif = imageio.get_reader("data/delorean-retroloop.gif")

duration = 0
frame_counter = 0

for frame in gif:
    frame_counter +=1
    duration += gif.get_meta_data(index=frame)["duration"]
    fps = frame_counter / (duration / 1000)

print(f"Total duration: {duration} ms")
print(f"Total number of frames: {frame_counter} frames")
print(f"Frames per second: {fps} fps")