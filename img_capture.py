import cv2, time
import matplotlib.pyplot as plt
video = cv2.VideoCapture(0)

if video.isOpened():
    ret, frame = video.read()
    print(ret)
    print(frame)
else:
    ret = False


img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.xticks([])
plt.yticks([])
plt.show()
video.release()    


