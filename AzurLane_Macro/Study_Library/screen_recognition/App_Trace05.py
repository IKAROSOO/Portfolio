import win32gui
import win32con
import mss
import time
import pyautogui as pag
import cv2
import numpy as np

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

Threshold = 0.75

def get_monitors():
    with mss.mss() as sct:
        monitors = sct.monitors
        monitor_list = []

        for i, monitor in enumerate(monitors, start=1):
            monitor_list.append({
                "left" : monitor["left"],
                "top" : monitor["top"],
                "width" : monitor["width"],
                "height" : monitor["height"],
                "mon" : i
            })
        
        return monitor_list

def click_center(top_left, btm_right):
    center_x = int((top_left[0]+btm_right[0])/2)
    center_y = int((top_left[1]+btm_right[1])/2)

    pag.click(center_x, center_y)

def Monitoring_Screen(title, template, templates):
    target_window = win32gui.FindWindow(None, title)

    if target_window == 0:
        print(f"No Winodw with title {title} found")
        return

    placement = win32gui.GetWindowPlacement(target_window)

    if placement[1] != win32con.SW_SHOWMAXIMIZED:
        win32gui.ShowWindow(target_window, win32con.SW_RESTORE)
    
    win32gui.SetForegroundWindow(target_window)
    
    target_window_size = win32gui.GetWindowRect(target_window)

    left, top, right, btm = target_window_size
    width = right - left
    height = btm - top

    capture_region = {
        "left" : left,
        "top" : top,
        "width" : width,
        "height" : height
    }
    # 캡쳐하는 범위를 while문의 외부에 둔 이유는 기본적으로 해당 매크로를 실행시키고, 해당 게임창을 움직이지 않을 것을 상정

    time.sleep(0.3)

    while True:
        with mss.mss() as sct:
            screenshot = sct.grab(capture_region)
        
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        for i, template in enumerate(templates):
            res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
            locate = np.where(res >= Threshold)

            for pt in zip(*locate[::-1]):
                top_left = pt
                btm_right = (top_left[0]+templates_size[i][0],
                             top_left[1]+templates_size[i][1])
                cv2.rectangle(frame, top_left, btm_right, color=(0, 255, 0), thickness=2)

                # click_center(top_left, btm_right)

        cv2.imshow("Test", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        time.sleep(0.01)

Monitoring_Screen("LDPlayer(64)", template, templates)

# 기존의 Monitoring 기능과 App Trace가 동시에 작동
# 하지만 아직까지는 전체화면이 아니면 Template이 정상적으로 작동하지 않는다.

# App_Trace04.py에서 변경된 곳은 98~105번 코드이다.
# 기존에는 imshow조차도 for문 내부에 있었기 때문에 Template이 없으면 동작을 멈췄다
# 이를 for문 외부로 꺼내는 것으로 해결