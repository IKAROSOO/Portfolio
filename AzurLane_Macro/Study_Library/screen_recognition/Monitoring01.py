import pyautogui as pag
import cv2
import time
import numpy as np
from PIL import Image

while True:
    screenshot = pag.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    cv2.imshow("Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # 'q' 키를 눌러서 종료

    time.sleep(0.5)

# 화면을 모니터링하는 기초적 코드