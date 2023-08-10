# YOLOv5-Implementaion-With-Static-Input
Introducing my image segmentation project, a script engineered to autonomously extract objects from images. 

1.1 INTRODUCTION

This documentation presents an overview of an image processing project that utilizes the YOLOv5 model for object detection and segmentation. The project focuses on automating the extraction of objects from static images, showcasing the integration of YOLOv5 with other technologies to achieve accurate and efficient results.

1.2 PROBLEM STATEMENT

The challenge addressed by this project is the need for precise and rapid object extraction from static images. Manual object identification and cropping are time-consuming and prone to errors, especially when dealing with large datasets. The project aims to provide a solution to this problem by implementing the YOLOv5 model, enabling automated and accurate object detection and segmentation.

1.3 FEATURES OF PROJECT

YOLOv5 Integration: The project leverages the YOLOv5 model, a state-of-the-art deep learning architecture, to detect and segment objects in images.

ResNet Pre-processing: The pre-trained ResNet model is used for additional image preprocessing, enhancing the accuracy of object detection.

Cropping and Saving: Detected objects are automatically cropped and saved, allowing for easy retrieval and further analysis.

Efficiency: The YOLOv5 model's high processing speed ensures quick and efficient object extraction, making the project suitable for real-time or batch processing scenarios.

1.4 PLATFORM/TECHNOLOGY

The project is developed using the following platform and technologies:

Python: The programming language used for implementing the project's codebase.

PyTorch: The deep learning framework utilized for integrating the YOLOv5 model into the project.

OpenCV: The computer vision library employed for reading and processing images.

Ultralytics YOLOv5: The YOLOv5 model is sourced from the Ultralytics repository, providing a seamless and efficient way to integrate the model into the project.

ResNet18: A pre-trained ResNet18 model is employed for enhancing image preprocessing and improving the accuracy of object detection.

The combination of these technologies forms a robust and effective framework for automating object extraction from static images, catering to various use cases in image processing and analysis.

1.5 TEST CASE:

INPUT IMAGE:
people.jpg:

![people](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/f9671480-ba3b-44cb-80fc-0cb1ee1e2047)

INTERNAL WORKING:

Convert to greyscale image:
![image0](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/4c1c1dcf-da65-4683-b290-aa46d804b610)

OUTPUT:

Files generated:

![WhatsApp Image 2023-08-10 at 11 08 01 PM (1)](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/b8edf856-d65e-49c0-af91-fe1fe9a8f051)

Segmented Images:

People Detected:

![image0](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/eb5f758e-8ab9-4915-8f65-083d9f6ce726)

![image02](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/79d09687-8196-49f6-8dc4-9bc507e0a9a7)

![image03](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/c13fbd34-8b4f-4461-9ef8-0404c05c3c9c)

![image04](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/f1163e74-a0dc-4e2e-b8df-eaa1c94f640f)

![image05](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/cb6040de-e095-48be-b543-a3b4ef07e6fb)

Bench Detected:

![image0](https://github.com/CodingNinja678/YOLOv5-Implementaion-With-Static-Input/assets/90537380/b0fb6d70-0334-42f8-ac92-26541c29caa0)




