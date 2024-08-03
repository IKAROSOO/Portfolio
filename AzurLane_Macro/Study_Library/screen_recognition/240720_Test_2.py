import pyautogui
import time

Lv1_img = "./Image/Lv1.png"
Lv2_img = "./Image/Lv2.png"
Lv3_img = "./Image/Lv3.png"
Lv4_img = "./Image/Lv4.png"

Test7 = "./screen_recognition/7.png"

a = pyautogui.locateOnScreen(Test7)
#내가 지정한 사진과 동일한게 화면에 있으면, 해당 사진의 좌표를 알려준다.
a_center = pyautogui.center(a)
#위의 좌표값은 (x, y, width, heitht)의 형태
#그 중심값으로 변경해준다.

# pyautogui.click(a_center)

b = pyautogui.locateCenterOnScreen(Test7)
#한번에 위의 2과정을 진행한다.
pyautogui.click(b)

#위의 모든 과정은 사진파일이 미리 존재하여야 한다.