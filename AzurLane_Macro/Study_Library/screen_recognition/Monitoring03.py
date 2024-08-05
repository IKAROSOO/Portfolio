import cv2
import numpy as np
import pyautogui as pag
import time

template_path = ['./AzurLane_Macro/Image/Neko.png', './AzurLane_Macro/Image/Oppai.png']
templates = []
templates_size = []

for path in template_path:
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    templates.append(template)
    templates_size.append(template.shape[::-1])

Threshold = 0.85

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
    
    cv2.imshow("Test", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# 한 번에 여러 개의 타겟을 잡는 것에 성공