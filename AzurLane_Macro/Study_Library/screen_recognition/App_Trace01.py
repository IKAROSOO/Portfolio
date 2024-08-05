import pygetwindow as gw
from PIL import ImageGrab
import numpy as np
import pyautogui as pag
import cv2
import time

def capture_window(title):
    windows = gw.getWindowsWithTitle(title)

    if not windows:
        print(f"No window with title '{title}' found")
        return

    window = windows[0]

    left, top, width, height = window.left, window.top, window.width, window.height

    screenshot = pag.screenshot(region=(left, top, width, height))

    screenshot.save("window_capture.png")

capture_window('LDPlayer(64)')

# 해당 방법을 사용하면 정확히 게임 앱만을 캡쳐한다
# 하지만 창을 최소화 시켜놓으면 추적이 불가능해서, 그저 모니터의 스크린샷이 된다.
# 또한 듀얼모니터도 지원하지 않는다. -> pyautogui의 screenshot함수의 문제