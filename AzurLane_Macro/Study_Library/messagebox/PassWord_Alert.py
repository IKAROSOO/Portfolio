import pyautogui

btn_5 = pyautogui.password(title="Password", text="Enter Your Password",
                           mask="@")
# 비밀번호 입력처럼 ***로 나온다.
print(btn_5)
# 출력은 정상적으로 입력한 것이 출력

if btn_5 == '1234':
    print("You are User!\nWelcome!!")
else:
    print("Get the FUCKOFF ASSHOLE")