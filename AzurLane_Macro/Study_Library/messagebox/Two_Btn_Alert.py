import pyautogui

btn_2 = pyautogui.confirm("Test")
#OK, CANCEL 2개의 선택지가 나온다.

print(btn_2)
# 내가 누른 버튼이 출력된다.

if btn_2 == "OK":
    print("Pressed OK")
else :
    print("Pressed CANCEL")