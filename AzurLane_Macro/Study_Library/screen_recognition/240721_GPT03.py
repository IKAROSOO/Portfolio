import cv2
import mss
import time
import numpy as np
import pyautogui as pag

btn_Go = "./Image/Go.png"
btn_Main = "./Image/Main.png"
btn_Home = "./Image/Home.png"
btn_124 = "./Image/12_4.png"
btn_Attack = "./Image/Attack.png"

Enemy_2 = "./Image/Lv2.png"

Supply = "./Image/Supply.png"

with mss.mss() as sct:
    monitors = sct.monitors

monitor_0 = {
    "left": monitors[0]['left'],
    "top": monitors[0]['top'],
    "width": monitors[0]['width'],
    "height": monitors[0]['height'],
    "mon": 1
}
monitor_1 = {
    "left": monitors[1]['left'],
    "top": monitors[1]['top'],
    "width": monitors[1]['width'],
    "height": monitors[1]['height'],
    "mon": 1
}
monitor_2 = {
    "left": monitors[2]['left'],
    "top": monitors[2]['top'],
    "width": monitors[2]['width'],
    "height": monitors[2]['height'],
    "mon": 2
}

def Search_Click(target_img_path):
    target_img = cv2.imread(target_img_path, cv2.IMREAD_GRAYSCALE)

    with mss.mss() as sct:
        screenshot = np.array(sct.grab(monitor_0))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGRA2GRAY)

    # 다양한 스케일 비율 시도
    found = None
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        resized = cv2.resize(target_img, (int(target_img.shape[1] * scale), int(target_img.shape[0] * scale)))
        r = target_img.shape[1] / float(resized.shape[1])
        if resized.shape[0] > screenshot.shape[0] or resized.shape[1] > screenshot.shape[1]:
            continue

        result = cv2.matchTemplate(screenshot, resized, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        locate = np.where(result >= threshold)
        locate = list(zip(*locate[::-1]))

        if locate:
            for loc in locate:
                x = loc[0] + resized.shape[1] // 2
                y = loc[1] + resized.shape[0] // 2
                pag.click(monitor_0["left"] + int(x * r), monitor_0["top"] + int(y * r))
                print(str(int(x * r)) + ', ' + str(int(y * r)))
                return
    print("일치하는 곳 없음")
    time.sleep(1)

# Search_Click(btn_Go)
# Search_Click(btn_Main)
Search_Click(btn_124)
Search_Click(btn_Attack)
