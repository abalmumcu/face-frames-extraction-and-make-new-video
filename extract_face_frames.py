from cv2 import cv2
import dlib


cap = cv2.VideoCapture('video.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

detector = dlib.get_frontal_face_detector()

if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(cap.isOpened()): 
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    img_no = 1

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
    if faces is not None:
      name = "faces\file_" + str(img_no) + ".png"
      cv2.imwrite(name, frame)
      img_no = img_no + 1    
        
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
      
