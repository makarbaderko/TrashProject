import serial, time
import cv2
import matplotlib.pyplot as plt
import tensorflow.keras
from PIL import Image
import numpy as np

video = cv2.VideoCapture(0)
def capture():
    global video
    if video.isOpened():
        ret, frame = video.read()
    else:
        ret = False
    #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.imwrite('capture.jpg', frame)
    #print(img)
    return 'capture.jpg'

def recognize(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = tensorflow.keras.models.load_model('keras_model.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(img)

    # Make sure to resize all images to 224, 224 otherwise they won't fit in the array
    image = image.resize((224, 224))
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array
    CATEGORIES = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
    # run the inference
    prediction = list(model.predict(data)[0])

    #print(CATEGORIES[prediction.index(max(prediction))])
    return CATEGORIES[prediction.index(max(prediction))]

serialcomm = serial.Serial('/dev/tty.wchusbserialfd120', 9600)
serialcomm.timeout = 1

while True:
    CATEGORIES = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
    photo = capture()
    i = recognize(photo)
    ans = 0
    for a in CATEGORIES:
        if a == i:
            ans = a
    serialcomm.write(ans.encode())
    time.sleep(0.5)
    #print(serialcomm.readline().decode('ascii'))
    print(i)
serialcomm.close()


