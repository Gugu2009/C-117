import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width, height)

fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('output.mp4', fourcc,20.0,(640,480))

for i in range(count -1,0,-1):
   frame = cv2.imread(images[1])
   out.write(frame)
out.release()
print("concluido")


