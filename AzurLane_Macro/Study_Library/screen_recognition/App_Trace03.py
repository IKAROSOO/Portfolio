import win32gui
import win32con
import mss
import time

with mss.mss() as sct:
    monitors = sct.monitors

monitor_0 = {
    "left": monitors[0]['left'],
    "top": monitors[0]['top'],
    "width": monitors[0]['width'],
    "height": monitors[0]['height'],
    "mon": 0
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

def capture_screen(title):
    target = win32gui.FindWindow(None, title)

    if target == 0:
        print(f"No window with title '{title}' found")
        return

    placement = win32gui.GetWindowPlacement(target)

    if placement[1] == win32con.SW_SHOWMAXIMIZED:
        print("Hello")
    else:
        # 최소화된 창을 복구한다.
        win32gui.ShowWindow(target, win32con.SW_RESOTRE)

    win32gui.SetForegroundWindow(target)
    # 지정된 창을 최상단으로 가져온다.

    target_size = win32gui.GetWindowRect(target)
    
    left, top, right, btm = target_size
    width = right - left
    height = btm - top

    capture_region = {
        "left" : left,
        "top" : top,
        "width" : width,
        "height" : height
    }

    time.sleep(0.3)

    with mss.mss() as sct:
        screenshot = sct.grab(capture_region)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output="Window_Capture.png")

capture_screen("Image")

# 캡쳐하는 함수를 pyautogui에서 mss로 변경하여 듀얼모니터의 캡쳐도 성공