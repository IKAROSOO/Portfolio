import cv2
import numpy as np
import pyautogui as pag
import time


template_path = ['./AzurLane_Macro/Image/Go.png']
templates = []
templates_size = []

for path in template_path:
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    templates.append(template)
    templates_size.append(template.shape[::-1])

Threshold = 0.85

def click_center(top_left, btm_right):
    center_x = int((top_left[0] + btm_right[0])/2)
    center_y = int((top_left[1] + btm_right[1])/2)

    print(f"Center of X : {center_x}, Center ot Y : {center_y}")

    pag.click(center_x, center_y)
    time.sleep(1)

while True:
    screenshot = pag.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    for i, template in enumerate(templates):
        res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

        locate = np.where(res >= Threshold)

        for pt in zip(*locate[::-1]):
            top_left = pt
            btm_right = (top_left[0] + templates_size[i][0], top_left[1] + templates_size[i][1])
            cv2.rectangle(frame, top_left, btm_right, (0, 0, 255), 1)
            click_center(top_left, btm_right)

    
    cv2.imshow("Test", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# 지정한 버튼을 사진으로 설정 시 해당 사진 위치의 좌표값을 읽어내는 것 성공
# 해당 좌표값을 기준으로, 클릭을 하게 하는 것은 성공
# 개선점 1 : 한번 클릭을 하게 되면 프로그램이 time.sleep만큼 정지할 뿐 아니라 클릭한 곳을 정지되어 있는 동안 계속 클릭
# 개선점 2 : 아직 게임화면을 인식에 성공시키려면 전체화면이 유지되어야만 함