#import module
import imageio

gif = imageio.get_reader("data/delorean-retroloop.gif")

duration = 0

for frame in gif:
    duration += gif.get_meta_data(index=frame)["duration"]

print(f"Total duration: {duration} ms")