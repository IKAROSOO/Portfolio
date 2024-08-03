import pyautogui
import cv2
import numpy as np
import random

# 스크린샷을 찍어 OpenCV 이미지로 변환
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

# 찾고자 하는 이미지 로드
needle_img = cv2.imread('./Image/TeamSelect', cv2.IMREAD_GRAYSCALE)

# 템플릿 매칭 수행
result = cv2.matchTemplate(screenshot, needle_img, cv2.TM_CCOEFF_NORMED)

# 유사도의 임계값 설정 (예: 0.8)
threshold = 0.8
locations = np.where(result >= threshold)

# 일치하는 위치의 중앙 좌표 계산
locations = list(zip(*locations[::-1]))

if locations:
    # 임의의 일치 항목 선택
    loc = random.choice(locations)
    center_x = loc[0] + needle_img.shape[1] // 2
    center_y = loc[1] + needle_img.shape[0] // 2
    print(f'Found at ({center_x}, {center_y})')

    # 찾은 위치에 사각형 그리기
    cv2.rectangle(screenshot, loc, (loc[0] + needle_img.shape[1], loc[1] + needle_img.shape[0]), (0, 255, 0), 2)

    # 해당 위치 클릭하기
    pyautogui.click(center_x, center_y)
else:
    print("No match found.")

# 결과 이미지 보여주기 (디버깅용)
cv2.imshow('Matches', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()


#GPT 작성 코드
# 일치하는 항목이 여러 개일 경우, 그 중 임의로 하나 선택하는 것