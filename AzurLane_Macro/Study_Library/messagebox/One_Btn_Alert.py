import pyautogui

btn_1 = pyautogui.alert(text="Hello, World!", title="It's Python", button="Turn Off")
# 1번은 경고문의 내용
# 2번은 alert창의 이름
# 3번은 내가 누를 버튼내용

print(btn_1)
# 3번이 출력
print(type(btn_1))
# 파일형 str