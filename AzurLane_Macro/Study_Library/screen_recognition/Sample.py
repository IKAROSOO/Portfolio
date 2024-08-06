import win32gui
import win32con
import mss
import time
import pyautogui as pag
import cv2
import numpy as np

template_info = [
    {"path": "./AzurLane_Macro/Image/Go.png", "label": "출격"},
    {"path": "./AzurLane_Macro/Image/Main.png", "label": "메인"},
    {"path": "./AzurLane_Macro/Image/12_4.png", "label": "12-4 출격"},
    {"path": "./AzurLane_Macro/Image/Attack.png", "label": "바로가기"}
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

def get_window_rect(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        print(f"No Window with title {title} found")
        return None
    
    win32gui.SetForegroundWindow(hwnd)
    rect = win32gui.GetWindowRect(hwnd)
    return rect

def click_center(top_left, btm_right):
    center_x = int((top_left[0] + btm_right[0]) / 2)
    center_y = int((top_left[1] + btm_right[1]) / 2)
    pag.click(center_x, center_y)

def Monitoring_Screen(title, templates, templates_size):
    rect = get_window_rect(title)
    if rect is None:
        return

    left, top, right, bottom = rect
    width = right - left
    height = bottom - top

    capture_region = {
        "left": left,
        "top": top,
        "width": width,
        "height": height
    }

    time.sleep(0.3)

    with mss.mss() as sct:
        while True:
            screenshot = sct.grab(capture_region)
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

            for i, template in enumerate(templates):
                res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
                locate = np.where(res >= Threshold)

                for pt in zip(*locate[::-1]):
                    top_left = pt
                    btm_right = (top_left[0] + templates_size[i][0],
                                 top_left[1] + templates_size[i][1])
                    cv2.rectangle(frame, top_left, btm_right, color=(0, 255, 0), thickness=2)

                    # click_center(top_left, btm_right)

            cv2.imshow("Test", frame)
            key = cv2.waitKey(10) & 0xFF

            if key == ord('q'):
                break

            time.sleep(0.01)

    cv2.destroyAllWindows()

Monitoring_Screen("LDPlayer(64)", templates, templates_size)
