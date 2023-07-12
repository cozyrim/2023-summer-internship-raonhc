import cv2
# opencv 라이브러리 import
webcam = cv2.VideoCapture(0)
# VideoCapture 객체 생성
if not webcam.isOpened():
    print("Could not open webcam")
    exit()
#
while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release() # 웹캠과의 연결 끊음
cv2.destroyAllWindows() # 웹캠을 보여주기 위해 생성했던 창 없앰 
