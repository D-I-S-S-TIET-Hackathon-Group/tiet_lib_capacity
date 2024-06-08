import cv2_imshow
import cv2

capture = cv2.VideoCapture('/content/drive/MyDrive/libvid.mp4')

if capture.isOpened():
    delay_time = 1000  # Delay time for 1 fps

    while True:
        isTrue, frame = capture.read()
        if not isTrue:
            print("Error: Could not read frame.")
            break
        cv2_imshow(frame)  # Keep this line for displaying frame
        if cv2.waitKey(delay_time) & 0xFF == ord('d'):
            break

else:
    print("Error: Could not open video.")

capture.release()
cv2.destroyAllWindows()


import os
dataset_dir = '/content/drive/MyDrive/dataset/'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

data_yaml = """
train: from google.colab import drive
drive.mount('/content/drive')
!git clone https://github.com/ultralytics/ultralytics.git
nc: 2  
names: ['chair unoccupied', 'occupied'] 

train: '/content/drive/MyDrive/Labelled images.zip' 
#val: '/content/drive/MyDrive/your_folder/val'  # Folder containing labeled validation images (optional for evaluation)

# Input image resolution
img_size: [848, 478]  # Adjust if needed based on your image size

# Other hyperparameters (learning rate, batch size, etc.)
# Refer to YOLOv8 documentation for detailed explanations of these parameters
hyp: 'data/yolov8s.yaml'  # Start with a pre-trained model's hyperparameters (e.g., yolov8s.yaml)
val: /content/drive/MyDrive/lib.zip

nc: 2 
names: ['occupied chair', 'unoccupied chair']
"""

with open(os.path.join(dataset_dir, 'library.yaml'), 'w') as f:
     f.write(data_yaml)


from ultralytics import YOLO

model = YOLO('yolov8n.pt')  

data_dir = '/content/train.txt'

model.train(data=data_dir, epochs=50, batch=16) 

model.save('seat_detection_model.pt')

