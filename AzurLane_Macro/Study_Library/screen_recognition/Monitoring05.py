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

for info in template_info:
    template = cv2.imread(info["path"], cv2.IMREAD_GRAYSCALE)
    templates.append(template)
    templates_size.append(template.shape[::-1])
    labels.append(info["label"])

Threshold = 0.85

def click_center(top_left, btm_right, label):
    center_x = int((top_left[0] + btm_right[0]) / 2)
    center_y = int((top_left[1] + btm_right[1]) / 2)

    print(f"Clicked on: {label} at Center of X : {center_x}, Center of Y : {center_y}")

    pag.click(center_x, center_y)

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

            # click_center(top_left, btm_right, labels[i])

    cv2.imshow("Test", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    time.sleep(0.01)

cv2.destroyAllWindows()

# 각 template 별로 라벨링 하는 것 성공
# 그에 따른 초기화면에서 출격까지 한번에 진행에 성공
# 하지만 아직은 template과 비교하여 존재하면 클릭하는 수준. -> 기준없이 막 클릭함