import win32gui
import win32con
import pyautogui
from PIL import Image
import time

def capture_minimized_window(title):
    # 창 핸들을 얻기 위해 `FindWindow`를 호출합니다.
    hwnd = win32gui.FindWindow(None, title)

    if hwnd == 0:
        print(f"No window with title '{title}' found.")
        return

    # 창을 복원합니다.
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

    # 창의 위치와 크기를 가져옵니다.
    rect = win32gui.GetWindowRect(hwnd)
    left, top, right, bottom = rect
    width = right - left
    height = bottom - top

    time.sleep(0.5)

    # 해당 위치와 크기로 화면을 캡처합니다.
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # 이미지를 파일로 저장합니다.
    screenshot.save("window_capture.png")
    print(f"Captured window '{title}' and saved as 'window_capture.png'.")

# 원하는 창의 제목을 입력합니다.
capture_minimized_window("LDPlayer(64)")  # 예를 들어, '메모장' 창을 캡처하려면 제목을 정확히 입력해야 합니다.

# 해당 방법은 최소화 되어있는 창을 끄집어 낸 후 캡쳐를 하는 방식이다.