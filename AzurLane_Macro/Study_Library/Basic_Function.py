import pyautogui

#마우스 포인터의 위치를 표시해주는 함수
pyautogui.position()

#마우스 움직이는 함수
#pyautogui.moveTo(141,429)

#위의 함수에서 이동하는 시간 추가
#pyautogui.moveTo(141, 444, 2)

#현재 마우스의 위치를 기준으로 좌표값만큼 이동
#pyautogui.moveRel(300, 300, 0.5)

pyautogui.moveTo(x=665, y=988)

#해당 위치를 클릭함
pyautogui.click(x=30, y=100)

# 설정된 문장을 입력, 한글은 입력되지 않는다. -> ASCII Code만 가능
pyautogui.typewrite("Hello!!, 한글 테스트")