import cv2
import numpy as np
import pyautogui 
from ultralytics import YOLO 


model = YOLO("bruh/my_model.pt")


cap = cv2.VideoCapture(0)


last_detected = ""
cooldown = 20  
counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break


    results = model(frame)

    annotated_frame = results[0].plot()
    
    resized_frame = cv2.resize(annotated_frame, (1280, 960))
    cv2.imshow("YOLOv8 Detection",    resized_frame)

    
    if results[0].boxes is not None:
        names = model.names  
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            detected_label = names[cls_id]  

            if detected_label != last_detected or counter >= cooldown:
                pyautogui.write(detected_label)
                last_detected = detected_label
                counter = 0
            break  

    counter += 1

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
