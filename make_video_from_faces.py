import os
from os.path import isfile, join
import cv2

cap = cv2.VideoCapture('video.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
pathIn= './video_processing/faces/'

frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
files.sort(key = lambda x: int(os.path.splitext(x)[0]))
for i in range(len(files)):
    filename=pathIn + files[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)

print(len(frame_array))
out = cv2.VideoWriter('output.mp4',0x7634706d , fps,size,True) 

for i in range(len(frame_array)):
    out.write(frame_array[i])
out.release()
