import pyautogui as pag
import time

btn_Go = (-243, 645, 220, 231)
btn_Main = (-1663, 183, 505, 647)
btn_12_4 = (-624, 773, 349, 66)

btn_Attack_1 = (-639, 732, 301, 103)
btn_Attack_2 = (-450, 824, 304, 96)

btn_Team_1 = (-391, 285, 99, 91)
btn_Team_1_3 = (-401, 530, 255, 52)
btn_Team_1_4 = (-401, 593, 255, 52)
btn_Team_1_5 = (-401, 656, 255, 52)

btn_Team_2 = (-391, 457, 99, 91)
btn_Team_2_6 = (-401, 890, 255, 52)

pag.click(pag.center(btn_Go))
time.sleep(0.5)
pag.click(pag.center(btn_Main))
time.sleep(0.5)
pag.click(pag.center(btn_12_4))
time.sleep(0.5)
pag.click(pag.center(btn_Attack_1))
time.sleep(0.5)
pag.click(pag.center(btn_Team_1))
time.sleep(0.5)
pag.click(pag.center(btn_Team_1_3))
time.sleep(0.5)
pag.click(pag.center(btn_Team_2))
time.sleep(0.5)
pag.click(pag.center(btn_Team_2_6))
time.sleep(0.5)
pag.click(pag.center(btn_Attack_2))
time.sleep(0.5)

# while True:
#     x, y = pag.position()
#     position_str = "X : " + str(x) + ", Y : " + str(y)
#     print(position_str)
#     time.sleep(0.1)