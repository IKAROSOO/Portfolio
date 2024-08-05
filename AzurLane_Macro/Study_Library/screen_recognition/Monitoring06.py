import cv2
import numpy as np
import pyautogui as pag
import time

template_info = [
    {"path" : "./AzurLane_Macro/Image/Go.png", "label" : "출격"},
    {"path" : "./AzurLane_Macro/Image/Main.png", "label" : "메인"},
    {"path" : "./AzurLane_Macro/Image/12_4.png", "label" : "12-4 출격"},
    {"path" : "./AzurLane_Macro/Image/Attack.png", "label" : "바로가기"}
]

templates = []
templates_size = []
labels = []

Threshold = 0.75

def click_center(top_left, btm_right, label):
    center_x = int((top_left[0] + btm_right[0])/2)
    center_y = int((top_left[1] + btm_right[1])/2)

    print(f"Clicked {center_x}, {center_y}, Label : {label}")

    pag.click(center_x, center_y)

def Monitoring_Screen(template, templates):
    while True:
        screenshot = pag.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        for i, template in enumerate(templates):
            res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
            locate = np.where(res >= Threshold)

            for pt in zip(*locate[::-1]):
                top_left = pt
                btm_right = (top_left[0] + templates_size[i][0],
                             top_left[1] + templates_size[i][1])
                cv2.rectangle(frame, top_left, btm_right)

                # click_center(top_left, btm_right)
        cv2.imshow("Test", frame)

        key = cv2.wiatKey(1) & 0xFF

        if key == ord('q'):
            break
            
            time.sleep(0.01)

# 모니터의 화면을 추적하는 것이 아닌, 게임의 화면만을 추적하면 된다.
# 이에 따라 화면 전체 캡쳐가 아닌 다른 방법을 사용해 보기로 한다.