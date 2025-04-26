# 🌞 하계 현장 실습 프로젝트 (2023)

> 🚗 차량 번호판 객체 인식 및 Qt GUI 제작

---

## 📌 프로젝트 개요

2023년 라온에이치씨에서 진행한 하계 현장 실습 프로젝트입니다. 주요 목표는 다음과 같습니다.

- 실시간 영상 입력을 통한 객체 인식 시스템 개발
- YOLOv8 모델을 이용한 차량 번호판 객체 검출 및 OCR 처리
- PyQt 및 Qt Designer를 활용한 사용자 친화적 GUI 제작
- 다양한 데이터 분석 및 성능 평가

---

## 🛠️ 개발 환경

- **Python 3.9**
- PyTorch, OpenCV, YOLOv8, PyQt

**의존성 설치**
```bash
pip install -r requirements.txt
```

---

## 📂 디렉터리 구조

```plaintext
Summer-Field-Practice/
├── yolov8/                   # YOLOv8 모델 및 객체 인식 코드
├── good_model_yolov8/        # 학습된 YOLOv8 모델 가중치 파일
├── qt_designer/              # PyQt GUI 관련 파일
├── cnn필기체1.ipynb          # CNN 기반 필기체 인식 실험
├── 필기체.ipynb              # 다양한 필기체 데이터 실험
├── yolo_nas.ipynb            # YOLO-NAS 모델 성능 비교
├── 자동차번호판.ipynb        # 차량 번호판 객체 검출 및 OCR
├── 02카메라입력.py           # 카메라 입력 처리 예제
├── 03카메라파라미터조정.py   # 카메라 파라미터 보정 예제
├── 05합분할.py               # 이미지 히스토그램 균등화 및 분할
├── 06회전.py                 # 이미지 회전 처리
├── 07객체인식.py             # 객체 인식 기본 예제
├── README.md                 # 프로젝트 설명서
└── requirements.txt          # Python 패키지 의존성 목록
```

---

## 🚀 주요 기능 및 실행 방법

### 📷 카메라 입력 및 영상 처리

```bash
python 02카메라입력.py
```

### 📐 카메라 캘리브레이션

```bash
python 03카메라파라미터조정.py
```

### 🚗 차량 번호판 객체 인식 (YOLOv8)

```bash
cd yolov8
python detect.py --source 0 --weights ../good_model_yolov8/best.pt
```

### 📖 차량 번호판 OCR 및 분석 (Jupyter Notebook)

- `자동차번호판.ipynb` 노트북을 열고 셀을 차례로 실행

---

## 💻 PyQt GUI

Qt Designer를 통해 제작한 GUI로, 실시간 카메라 입력을 받아 객체 인식을 제공합니다.

- 위치: `qt_designer/main.py`
- 실행:

```bash
python qt_designer/main.py
```

**기능**
- 실시간 카메라 스트림 보기
- 객체 인식 실시간 확인
- 시작/정지 및 설정 관리

---

## 📑✏️ 일자별 보고서

| 날짜 | 보고서 링크 |
|------|------------|
| 7월 4일 (2일차) ~ 7월 31일 (21일차) | [7월 보고서 모음](https://www.notion.so/7-1e1e69e4b9b3807ca900e9a8524e71bb?pvs=4) |
| 8월 1일 (22일차) ~ 8월 29일 (40일차) | [8월 보고서 모음](https://www.notion.so/8-1e1e69e4b9b38027910bca7bd85d2020?pvs=4) |

> 각 날짜별 상세 보고서는 상단의 링크를 통해 확인 가능합니다.

---
