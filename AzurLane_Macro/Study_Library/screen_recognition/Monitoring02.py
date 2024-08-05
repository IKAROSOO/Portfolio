import cv2
import numpy as np
import time
import pyautogui as pag

template = cv2.imread('./AzurLane_Macro/Image/Neko.png', cv2.IMREAD_GRAYSCALE)
template_height, template_width = template.shape[:2]

Threshold = 0.8

def click_center(top_left, btm_right):
    center_x = int((top_left[0] + btm_right[0])/2)
    center_y = int((top_left[1] + btm_right[1])/2)

    print(f"Center of X : {center_x}, Center ot Y : {center_y}")

while True:
    screenshot = pag.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    locate = np.where(res >= Threshold)
    for pt in zip(*locate[::-1]):
        top_left = max_loc
        btm_right = (top_left[0] + template_width, top_left[1] + template_height)

        cv2.rectangle(frame, top_left, btm_right, (0, 255, 0), 2)
        click_center(top_left, btm_right)

    cv2.imshow("Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    time.sleep(0.1)

# 화면에서 템플릿 매치를 사용하는 코드
# Threshold를 사용해서 유사도의 임계값을 설정