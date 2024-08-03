import mss

with mss.mss() as sct:
    monitors = sct.monitors
    for i, monitor in enumerate(monitors):
        print(f"Monitor {i}: {monitor}")

# 모니터 정보를 출력한 후 올바른 설정을 적용합니다.
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

with mss.mss() as sct:
    # 스크린샷을 찍으려면 다음과 같이 하면 됩니다.
    img_0 = sct.grab(monitor_0)
    img_1 = sct.grab(monitor_1)
    img_2 = sct.grab(monitor_2)

    # 예시: 파일로 저장하기
    mss.tools.to_png(img_0.rgb, img_0.size, output="monitor_0.png")
    mss.tools.to_png(img_1.rgb, img_1.size, output="monitor_1.png")
    mss.tools.to_png(img_2.rgb, img_2.size, output="monitor_2.png")
