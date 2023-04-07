
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

print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,channel = frame.shape
print(height,width)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter("Project 105 - Video Album.mp4",fourcc,0.8,(width,height))
for i in range(0,count-1):
    frame1 = cv2.imread(images[i])
    out.write(frame1)

out.release()
cv2.destroyAllWindows()
print("Done")