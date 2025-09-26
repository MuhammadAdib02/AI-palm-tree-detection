from ultralytics import YOLO

def main():
    # Step 1: Load a pretrained YOLOv8 model
    model = YOLO("yolov8n.pt")  # Choose yolov8s.pt / yolov8m.pt if needed

    # Step 2: Train the model
    model.train(
        data="data.yaml",        # Path to your dataset config
        epochs=50,               # Number of training epochs
        imgsz=640,               # Image size
        batch=8,                 # Adjust depending on your GPU memory
        name="palm_tree_yolo"    # Output folder name
    )

    # Step 3: Validate the model
    model.val()

    # Step 4: Run prediction on a sample image
    results = model.predict(source="sample.jpg", save=True, conf=0.25)
    print("Prediction complete. Check the 'runs/detect/predict' folder for results.")

    # Step 5 (Optional): Export to ONNX for deployment
    # model.export(format='onnx')

if __name__ == "__main__":
    main()
