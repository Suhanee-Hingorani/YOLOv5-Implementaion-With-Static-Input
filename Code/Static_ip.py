# Import necessary libraries
import torch
from torchvision import models
import cv2

# Load pre-trained ResNet model
resnet_model = models.resnet18(pretrained=True)

# Load YOLOv5 model from Ultralytics
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Path to the input image
img_path = 'test.jpg'  # Replace with your image file path

# Initialize a counter for object instances
count = 0

# Read the input image using OpenCV
image = cv2.imread(img_path)

# Perform object detection using YOLOv5 model
results = model(image)

# Crop and save detected objects
results.crop(save_dir='./detection_data/' + str(img_path) + '/')  # Save cropped objects

# Note: Make sure the 'detection_data' directory exists in your working directory before running the script
