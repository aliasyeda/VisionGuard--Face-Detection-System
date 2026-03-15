# VisionGuard--Face-Detection-System

# Face Detection System

A Python-based face detection system using OpenCV that detects faces in images and real-time video.

## 📋 Project Overview
This project uses Haar Cascade Classifier to detect human faces in images and through webcam. It draws bounding boxes around detected faces and can handle multiple faces simultaneously.

## ✨ Features
- ✅ Detect faces in static images
- ✅ Real-time face detection using webcam  
- ✅ Multiple face detection in single frame
- ✅ Save output images with timestamps
- ✅ Simple menu-driven interface

## 🛠️ Technologies
- Python 3.9+
- OpenCV
- NumPy
- Haar Cascade Classifier

## ⚙️ Installation

```bash
# Install required packages
pip install opencv-python numpy
🚀 How to Run
bash
python face_detection.py
📖 Usage
Main Menu:
Detect Faces in Image - Enter image path when prompted

Live Webcam Detection - Press 'q' to quit, 's' to save

Exit - Close the program

Webcam Controls:
q - Quit webcam mode

s - Save current frame

📁 Project Structure
text
face-detection-system/
│
├── face_detection.py    # Main program
├── README.md           # Documentation
├── requirements.txt    # Dependencies
└── outputs/            # Saved results (auto-created)
💻 Code Example
python
import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read image
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show result
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
📊 Sample Output
text
Enter image path: test.jpg
✅ Found 2 face(s)
💾 Saved to: output_20240315_143022.jpg
⚠️ Troubleshooting
Issue	Solution
Module not found	Run pip install opencv-python numpy
No faces detected	Use clear image with visible faces
Webcam not working	Check camera connection
🔮 Future Improvements
Face recognition (identify specific people)

Video file processing

Gender and age detection

GUI interface



👤 Author
Syeda Alia Samia

🔗 GitHub
https://github.com/yourusername/face-detection-system

