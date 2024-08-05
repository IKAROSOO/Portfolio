import win32gui
import win32con
import pyautogui
from PIL import Image
import time

def capture_minimized_window(title):
    hwnd = win32gui.FindWindow(None, title)

    if hwnd == 0:
        print(f"No window with title '{title}' found.")
        return

    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

    rect = win32gui.GetWindowRect(hwnd)
    left, top, right, bottom = rect
    width = right - left
    height = bottom - top

    time.sleep(0.5)

    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    screenshot.save("window_capture.png")
    print(f"Captured window '{title}' and saved as 'window_capture.png'.")

capture_minimized_window("LDPlayer(64)")  # 예를 들어, '메모장' 창을 캡처하려면 제목을 정확히 입력해야 합니다.

# 해당 방법은 최소화 되어있는 창을 끄집어 낸 후 캡쳐를 하는 방식이다.