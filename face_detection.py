"""
VisionGuard - Advanced Face Detection System
A professional real-time face detection solution using OpenCV
Author: Syeda Alia samia
Version: 1.0.0
"""

import cv2
import numpy as np
import os
import sys
from datetime import datetime

class VisionGuard:
    """Professional Face Detection System"""
    
    def __init__(self):
        self.version = "1.0.0"
        self.author = "Syeda Alia Samia"
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        print(f"\n🔷 VisionGuard v{self.version} Initialized")
        print(f"👤 Author: {self.author}")
        print("✅ System Ready\n")
    
    def detect_image(self, image_path):
        """Detect faces in static image"""
        if not os.path.exists(image_path):
            print(f"❌ Error: Image not found - {image_path}")
            return
        
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            print("❌ Error: Cannot read image file")
            return
        
        # Process image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
        
        # Draw results
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(img, "FACE DETECTED", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Add stats
        stats = [
            f"Faces Detected: {len(faces)}",
            f"Time: {datetime.now().strftime('%H:%M:%S')}",
            f"Resolution: {img.shape[1]}x{img.shape[0]}"
        ]
        
        y_pos = 30
        for stat in stats:
            cv2.putText(img, stat, (10, y_pos), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y_pos += 30
        
        # Show result
        cv2.imshow('VisionGuard - Face Detection Result', img)
        print(f"📊 Analysis Complete: {len(faces)} face(s) found")
        print("Press any key to continue...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Save output
        output_name = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(output_name, img)
        print(f"💾 Result saved as: {output_name}")
        
        return len(faces)
    
    def detect_webcam(self):
        """Real-time face detection using webcam"""
        print("📹 Initializing webcam...")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Error: Cannot access webcam")
            return
        
        print("✅ Webcam ready - Press 'Q' to quit, 'S' to save snapshot")
        
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
            
            # Draw detections
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "FACE", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Draw HUD
            cv2.putText(frame, f"VisionGuard v{self.version}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(frame, f"Faces: {len(faces)}", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, "[Q]uit [S]ave", (10, 90),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            cv2.imshow('VisionGuard - Live Detection', frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                snapshot = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(snapshot, frame)
                print(f"📸 Snapshot saved: {snapshot}")
        
        cap.release()
        cv2.destroyAllWindows()
        print("👋 Webcam session ended")
    
    def batch_process(self, folder_path):
        """Process multiple images in a folder"""
        if not os.path.exists(folder_path):
            print(f"❌ Folder not found: {folder_path}")
            return
        
        images = [f for f in os.listdir(folder_path) 
                 if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if not images:
            print("❌ No images found in folder")
            return
        
        print(f"📁 Found {len(images)} images to process")
        results = {}
        
        for img_file in images:
            img_path = os.path.join(folder_path, img_file)
            faces = self.detect_image(img_path)
            results[img_file] = faces
            print(f"   • {img_file}: {faces} face(s)")
        
        # Save report
        report_path = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_path, 'w') as f:
            f.write("VisionGuard Batch Processing Report\n")
            f.write("="*40 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Images: {len(images)}\n\n")
            for img, count in results.items():
                f.write(f"{img}: {count} faces\n")
        
        print(f"📊 Report saved: {report_path}")

def main():
    """Main application entry point"""
    print("="*60)
    print("               VISIONGUARD")
    print("         Professional Face Detection System")
    print("="*60)
    
    detector = VisionGuard()
    
    while True:
        print("\n📌 MAIN MENU")
        print("-" * 40)
        print("1️⃣  Detect Faces in Single Image")
        print("2️⃣  Live Webcam Detection")
        print("3️⃣  Batch Process Folder")
        print("4️⃣  System Info")
        print("5️⃣  Exit")
        print("-" * 40)
        
        choice = input("👉 Enter your choice (1-5): ").strip()
        
        if choice == '1':
            path = input("📷 Enter image path: ").strip()
            detector.detect_image(path)
            
        elif choice == '2':
            detector.detect_webcam()
            
        elif choice == '3':
            folder = input("📁 Enter folder path: ").strip()
            detector.batch_process(folder)
            
        elif choice == '4':
            print("\n🔧 SYSTEM INFORMATION")
            print(f"Version: {detector.version}")
            print(f"Author: {detector.author}")
            print(f"OpenCV: {cv2.__version__}")
            print(f"NumPy: {np.__version__}")
            
        elif choice == '5':
            print("\n👋 Thank you for using VisionGuard!")
            print("Visit us on GitHub for updates\n")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program terminated by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please report this issue on GitHub")