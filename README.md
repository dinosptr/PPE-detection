# PPE Detection Model

## System Requirements
- Operating System: Windows, MacOS, or Linux
- Python 3.10
- Git
- Disk Space: At least 2GB available disk space

## Pre-installation Checks

1. *Check Python Installation:*
   - Open Command Prompt (cmd).
   - Check if Python is installed by running:
     
    ```bash
    python --version
    ```
     
   - If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/). Make sure to select the version compatible with your operating system.

2. *Check Git Installation:*
   - Check if Git is installed by running:
     ```bash
     git --version
     
   - If Git is not installed, download and install it from [git-scm.com](https://git-scm.com/downloads/).

## Installation Steps

# 3. Navigate to Project Folder in Command Prompt:
   - Change the current directory to your project folder using the cd command.

# 4. Create Virtual Environment and Project Folder:
   - Create a new folder named "ppe-project" using the following command:
     ```bash
     mkdir ppe-project
     
     
   - Navigate to the "ppe-project" folder:
     ```bash
     cd ppe-project
     
     
   - Create a new Python virtual environment named "your-env-name" using the following command:\
     ```bash
     python -m venv your-env-name 
     ```
     or 
     ```bash
     py -m venv your-env-name
     ```
     
     Activate the virtual environment:
     - On Windows:
       ```bash
       .\your-env-name\Scripts\activate
       
       
     - On MacOS/Linux:
       ```bash
       source your-env-name/bin/activate
       

Now you have set up a project folder named "ppe-project" with a Python virtual environment named "your-env-name." Next, proceed with the remaining installation steps within this project folder.

# 5. Clone Project Files:
   - Clone the project repository containing notebook files and the pre-trained model "best.pt" from GitHub with the following command:
     ```bash
     git clone https://github.com/dinosptr/PPE-detection.git
     

   - Navigate to the cloned repository folder:
     ```bash
     cd PPE-detection
     

# 6. Create 'ppe' Folder and Clone YOLOv8 (Ultralytics Version):

   - install YOLOv8 (Ultralytics Version) with pip following command:
     ```bash
     pip install ultralytics
     
# 7. Running Code
Now, you can run the YOLOv8 prediction using the provided examples. Make sure to replace "file.pt" and "path/to/image.jpg" with your actual model file path and image file path, respectively.

Example:
```bash
yolo predict model="model/best.pt" imgsz=640 conf=0.25 source=0 show=True ✅

yolo predict model="model/best.pt" imgsz=640 conf=0.25 source="path/to/image.jpg" show=True✅

yolo predict --model yolov8n.pt --imgsz 640 --conf 0.25 ❌
```

## Parameters
- model: Path to the yolov8 model file.
- imgsz: Input image size (in pixels).
- conf: Confidence threshold for object detection.
- source: Path to input image or video and can a webcam.
- show: If True, displays the annotated images or videos in a window. Useful for immediate visual feedback during development or testing.

*Note:* For the source parameter, you can provide the following values:
- For Webcam: Use source=0 for default webcam or specify the webcam index .
- For Image: Path to a single image file (e.g., source=" path/to/image.jpg").
- For Video: Path to a video file (e.g., source="path/to/video.mp4").

# 8. Example Output
![Alt text](assets/giphy(1).gif)
![Alt text](assets/giphy(2).gif)
![Alt text](assets/giphy(3).gif)
![Alt text](assets/giphy(4).gif)
