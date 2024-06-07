import numpy as np
import cv2

img_path = 'training_imgs/'
proto_path = 'models/MobileNetSSD_deploy.prototxt.txt'
model_path = 'models/MobileNetSSD_deploy.caffemodel'

min_confidence = 0.2

classes = ["chair"]

np.random.seed(8008135)
colors = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv2.dnn.readNetFromCaffe(proto_path, model_path)

img = cv2.imread(img_path)
h, w = img.shape[0], img.shape[1]
SCALE_FACTOR = 0.007
MEAN = 130
blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), SCALE_FACTOR, (300, 300), MEAN)

net.setInput(blob)
detected_obj = net.forward()

for i in range(detected_obj.shape[2]):
    confidence = detected_obj[0][0][i][2]
    if confidence > min_confidence:
        ind = int(detected_obj[0][0][i][1])

        upper_left_x = int(detected_obj[0][0][i][3] * w)
        upper_left_y = int(detected_obj[0][0][i][4] * h)
        lower_right_x = int(detected_obj[0][0][i][5] * w)
        lower_right_y = int(detected_obj[0][0][i][6] * h)

        txt = f"{classes[ind]}: {confidence:.3f}%"

        cv2.rectangle(img, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors[ind], 3)
        cv2.putText(img,
                    txt,
                    (upper_left_x,
                    upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[ind], 2
                    )
        
    cv2.imshow("DETECTED OBJECTS", img)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

