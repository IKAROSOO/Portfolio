import pyautogui as pag

btn = pag.confirm(text="Hello, World!!", title="Test",
                  buttons=["First", "Second", "Third"])

print(btn)      # 클릭한 값이 출력