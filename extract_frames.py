import cv2
import glob
from glob import glob
import os
import shutil

def extractFrames(m,n):
    if not os.path.exists:
        os.makedirs(n)

    vid_files=glob(m)
    print(vid_files)

    for v_f in range(len(vid_files)):
        v1=os.path.basename(vid_files[v_f])
        print(v1)
        vid_name = os.path.splitext(v1)[0]
        print(vid_name)
        output = n +'\\video_' + vid_name
        os.makedirs(output)
        print(output)


        vidcap = cv2.VideoCapture(vid_files[v_f])
        print(vidcap)
        success,image = vidcap.read()
        seconds = 2
        fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
        multiplier = fps * seconds
        count=0

        while success:
            img_name = vid_name + '_f' + str(count) + ".jpg"
            image_path = output + "/" + img_name
            frameId = int(round(vidcap.get(1)))
            success,image = vidcap.read()
            if frameId % multiplier == 0:
                cv2.imwrite(filename = image_path, img = image)
                count+=1

        vidcap.release()
        cv2.destroyAllWindows()

        print('finished processing video {0} with frames {1}'.format(vid_files[v_f], count))
    return output # indent this less

x=("C:\\Users\\ALPER\\Desktop\\python\\video.mp4")
y=("C:\\Users\\ALPER\\Desktop\\python\\video_processing\\faces")

z=extractFrames(x,y)