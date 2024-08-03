import pyautogui

btn_4 = pyautogui.prompt(title="Test", default="It's Python", text="HI!")
print(btn_4)
# 내가 입력한 값이 출력된다. -> input() 대신 사용가능
# Cancel을 누르면 None이 된다.