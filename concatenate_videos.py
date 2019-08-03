import os
import sys

def create_video(_path):
    text_file_path = _path + "/videos.txt"
    with open(text_file_path, "w") as text_file:
        for r, d, f in os.walk(_path):
            for file in f:
                if '.mp4' in file:
                    # files.append("file '{}'".format(file))
                    text_file.write("file '{}'\n".format(file))

    os.system("ffmpeg -f concat -safe 0 -i {} -c copy video.mp4".format(text_file_path))

try:
    path = sys.argv[1]
    create_video(path)
except:
    print("ERROR: Please provide video path!")