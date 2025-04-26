import cv2
import numpy as np

def imgShow():
    imgFile = "fruit.webp"
    img = cv2.imread(imgFile)

    b, g, r = cv2.split(img) #이미지 분할 

    cv2.imshow('blue',b)
    cv2.imshow('Green',g)
    cv2.imshow('Red',r)

    merged_img = cv2.merge((b,g,r)) #이미지 합치기
    cv2.imshow('merge',merged_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() # 인자로 받은 윈도우 핸들을 통해 윈도우 파괴함수
   

imgShow()

