import pyautogui

pyautogui.screenshot("./screen_recognition/1.png", region=(1587, 597, 30, 30))
#입력해 놓은 region은 앞의 2개가 x, y값
#두 좌표를 기준으로 뒤의 2개가 width, height만큼 캡쳐해서 저장

num1 = pyautogui.locateOnScreen("./screen_recognition/1.png")
pyautogui.click(num1)