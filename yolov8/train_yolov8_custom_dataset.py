from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2,torch
# model = YOLO("yolov8n.yaml")
# model = YOLO("C:/Users/cofla/yolov8/runs/detect/train27/weights/best.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolov8n.pt")

if __name__ == '__main__':
    # Use the model

    results = model.train(data="C:/Users/cofla/yolov8/data.yaml", epochs=30, imgsz=640)  # train the model
    results = model.val()  # evaluate model performance on the validation set
    results = model.predict("C:/Users/cofla/yolov8/test/images/01-1316_jpg.rf.3b8364a7284db2c5e7c7cb666e065a3d.jpg", save = True)  # predict on an image
    # success = YOLO("yolov8n.pt").export(format="onnx")  # export a model to ONNX format
    # results = model.predict(source='/content/crosswalk-models-1/test/images/', save=True)
