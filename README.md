# Real-time Face Detection using OpenCV in Python

The Real-time Face Detection project is a computer vision-based application developed in Python using OpenCV. The project aims to detect faces in a live video stream and draw a green rectangle box around each detected face. Additionally, the project dynamically updates the text displayed on the video feed from "No" to "Face Detected" whenever a face is detected. The program terminates and closes the camera when the 'Esc' button is pressed.

## Key Features

1. **Video Capture**: The project utilizes the OpenCV library to capture a live video stream from a camera.

2. **Face Detection**: Upon launching the application, the live video stream is continuously processed to detect faces using Haar cascades or deep learning-based face detection models. When a face is detected, a green rectangle box is drawn around it.

3. **Dynamic Display**: The video feed is dynamically updated to display the text "No" when no face is detected. As soon as a face is detected, the text is changed to "Face Detected", indicating the presence of a face in the video stream.

4. **User Interaction**: The program can be terminated by pressing the 'Esc' button on the keyboard. This action closes the camera and ends the execution of the application.

## Usage

1. Clone the repository:

```bash
git clone <>
