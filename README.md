# 🌞 2023 하계 현장 실습 프로젝트 – 라온에이치씨 (RaonHC)

> 🚗 실시간 차량 번호판 객체 인식 및 PyQt GUI 제작



## 📌 프로젝트 개요

2023년 라온에이치씨에서 진행한 하계 현장 실습 프로젝트입니다. 주요 목표는 다음과 같습니다.

- OpenCV 기반 실시간 영상 입력 및 전처리  
- YOLOv8 / YOLOv3 / YOLO-NAS 모델을 활용한 객체 검출  
- OCR을 통한 차량 번호판 인식  
- PyQt(Qt Designer) 기반 GUI 제작  
- 다양한 데이터 분석 및 성능 평가


## 🛠️ 개발 환경 및 설치

- **Python 3.9**  
- 주요 라이브러리: PyTorch, OpenCV, PyQt5, ultralytics(YOLOv8) 등

**의존성 설치**
```bash
pip install -r requirements.txt
```


## 📂 디렉터리 구조

```plaintext
2023-summer-internship-raonhc/
├── qt_designer/                          
├── yolov8/                               
├── 02_opencv_webcam_stream.py            
├── 03_camera_calibration_basic.py        
├── 03_camera_calibration_multi_image.py  
├── 03_camera_calibration_optimized.py    
├── 03_camera_calibration_undistort.py    
├── 04_face_detection_camera.py           
├── 05_image_channel_split_merge.py       
├── 06_image_rotation_transform.py        
├── 07_object_detection_yolov3.py         
├── handwriting_classification_cnn.ipynb  
├── handwriting_dataset_exploration.ipynb 
├── license_plate_detection_ocr.ipynb     
├── object_detection_yolo_nas.ipynb       
├── requirements.txt                      
└── README.md                             
```


## 🚀 주요 기능 및 실행 방법

### 📷 카메라 입력 및 영상 처리

```bash
python 02_opencv_webcam_stream.py
```

### 📐 카메라 캘리브레이션

```bash
python 03_camera_calibration_basic.py --image path/to/checkerboard.jpg
python 03_camera_calibration_multi_image.py --dir path/to/checkerboard_images
python 03_camera_calibration_undistort.py --dir path/to/checkerboard_images
```

### 🚗 차량 번호판 객체 인식 (YOLOv8)

```bash
cd yolov8
python detect.py --source 0 --weights ../good_model_yolov8/best.pt
```

### 📖 차량 번호판 OCR 및 분석 (Jupyter Notebook)

- `자동차번호판.ipynb` 노트북을 열고 셀을 차례로 실행



## 💻 PyQt GUI

Qt Designer를 통해 제작한 GUI로, 실시간 카메라 입력을 받아 객체 인식을 제공합니다.

- 위치: `qt_designer/main.py`
- 실행:

```bash
python qt_designer/main.py
```

**기능**
- 실시간 카메라 스트림 표시
- 객체 검출 결과 오버레이
- 시작/중지 버튼 및 설정 변경



## 📑✏️ 일자별 보고서

| 날짜 | 보고서 링크 |
|------|------------|
| 7월 4일 (2일차) ~ 7월 31일 (21일차) | [7월 보고서 모음](https://www.notion.so/7-1e1e69e4b9b3807ca900e9a8524e71bb?pvs=4) |
| 8월 1일 (22일차) ~ 8월 29일 (40일차) | [8월 보고서 모음](https://www.notion.so/8-1e1e69e4b9b38027910bca7bd85d2020?pvs=4) |

> 각 날짜별 상세 보고서는 상단의 링크를 통해 확인 가능합니다.


