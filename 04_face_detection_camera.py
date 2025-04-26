import cv2

# 카메라 호출, USB 카메라를 따로 사용하여 디바이스 순번 ID 1번  사용, 
# 기본 내장 카메라 는 보통 순번 ID 0 번 사용
vcap = cv2.VideoCapture(1) 

# 카메라 속성 설정
vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 세로 사이즈
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 가로 사이즈

# 얼굴 인식 / 검출 관련 모델(가중치) 파일
# [https://github.com/opencv/opencv/tree/master/data/haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)
casecade_xml = 'openCV_XML/haarcascade_frontalface_default.xml'

# 모델 파일 불러오기
face_cascade = cv2.CascadeClassifier(casecade_xml)

# 실시간 영상에서 얼굴 검출
def videoDetector(vcap, face_cascade) :
    faces_cnt = 0 # 검출 얼굴수
    # 카메라의 프레임을 지속적으로 받아오기
    while True :
        # vcap.read() 프레임 읽기 
        # ret 은 카메라 상태 이며, 정상 : True, 비정상 : False
        # frame 은 현재시점의 플레임 
        ret, frame = vcap.read()

        # #  숫자키 1 입력시 좌우 대칭 변경
        # if cv2.waitKey(1) == 49 :
        #     # 대칭 처리 
        #     # value < 0 상하좌우 대칭
        #     # value = 0 상하 대칭
        #     # value > 0  좌우 대칭
        #     frame = cv2.flip(frame, 1)
        frame = cv2.flip(frame, 1) # 좌우 대칭 변경

        # 영상 이미지를 그레이스케일로 이진화(검은색, 흰색{True, False})
        #  cv2.cvtColor(대상 이미지, 그레이 스케일)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 영상 이미지에서 얼굴 검출 하기
        #  gray                    # 대상 이미지 행렬
        # ,scaleFactor  = 1.1      # 이미지 피라미드 규모인자 크기(Scale Factor)
        # ,minNeighbors = 5        # 최종 검출영역 확정용 이웃 사각형의 갯수 설정
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        # 화면에 검출 된 얼굴 수 가 변경될때마다 출력
        if faces_cnt != len(faces) :
            faces_cnt = len(faces)
            if faces_cnt != 0 :
                print("현재 검출된 얼굴 수 : ", str(faces_cnt))

        # 검출된 안면에 사각형 그리기
        # cv2.rectangle(영상이미지, (x1, y1), (x2, y2), (B, G, R), 두깨, 선형타입)
        # (X1, Y1) 좌측 상단 모서리, (X2, Y2) 우측 하단 모서리.
        if len(faces) :
            for  x, y, w, h in faces :
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255,255,255), 2, cv2.LINE_4)

        # 윈도우창 (Title , 프레임 이미지)
        cv2.imshow("VideoFrame", frame)

        # cvs2.waitKey(1) 1은 밀리세컨으로 키입력값 대기 지연시간이다. ESC로 멈춤
        if cv2.waitKey(1) == 27 :
            vcap.release()          # 메모리 해제 
            cv2.destroyAllWindows() # 모든창 제거, 특정 창만듣을 경우 ("VideoFrame")
            break;                  


# 실시간 영상에서 얼굴 검출 호출
videoDetector(vcap, face_cascade)
