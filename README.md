# 🙌 ASL Interpreter: OpenCV YOLO Model Project

This project was originally inspired by JARVIS, the AI assistant from the Iron Man movies. Over time, its purpose evolved: rather than being a general AI, it was redesigned to assist people who have difficulty typing due to conditions like trigger finger or carpal tunnel syndrome by interpreting American Sign Language (ASL) hand signs into text and keyboard commands.

## Features
- **Real-time Letter Recognition**: Captures ASL letters shown to the camera and converts them into text automatically.  
- **Special Command Recognition**: Detects specific hand signs that correspond to keyboard functions like Enter, Space, or Delete.  
- **User-Friendly Python Implementation**: Built with Python
- **Cooldown Mechanism**: Prevents repeated key presses from continuous detection, ensuring smooth typing.  
- **Visual Feedback**: Displays the detection results on-screen with bounding boxes and labels for better user interaction.  

## Languages and Tools Used
- **Python 3.x**: The main programming language used for flexibility and rapid development.  
- **YOLOv8 by Ultralytics**: A real-time object detection model used for recognizing hand signs.  
- **OpenCV**: For video capturing, image processing, and displaying real-time feedback.  
- **PyAutoGUI**: Enables automated keyboard input by simulating key presses.  
- **NumPy**: For efficient numerical operations on image data.  

## Future Improvements
- Expand the vocabulary of recognized ASL signs.  
- Add voice feedback for detected words.  
- Integrate with text-to-speech for enhanced accessibility.  
- Optimize model for mobile and embedded devices.

Demonstration will be in the video link: 
