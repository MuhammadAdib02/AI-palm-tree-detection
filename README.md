# AI-palm-tree-detection
A drone-image analysis tool that uses YOLOv8 to automatically detect and count palm trees from aerial photos, enabling quick mapping and monitoring of plantations.

Brief description of the project.

## 📜 Project Overview
This project applies **YOLOv8 object detection** to locate and count palm trees from drone-captured images across various regions in Malaysia.  
The goal is to assist plantation management in mapping tree density and monitoring growth.

> **Note:** This was an internship project and remains an early prototype.  
> The trained model is functional but not yet production-ready.

---

## 📂 Repository Structure
- env/ # Local environment folder (not required to run)
- images/ # Sample output images and visualizations
- labels/ # YOLO labels for training
- results/ # Detection results and evaluation outputs
- runs/detect/ # YOLOv8 training/detection logs
- data.yaml # Dataset configuration file
- requirements.txt # Python dependencies
- split.py # Script to split dataset into train/val sets
- train_log.txt # Training log
- yolov8n.pt # Small YOLOv8 trained weights
- yolov8s.pt # Slightly larger YOLOv8 trained weights

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/palm-tree-detection.git
   cd palm-tree-detection
   python -m venv venv
   source venv/bin/activate      # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   yolo task=detect mode=predict model=yolov8n.pt source=images/




