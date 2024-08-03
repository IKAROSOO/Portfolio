import cv2
import numpy as np
import pyautogui

def capture_screen(region=None):
    """현재 화면의 스크린샷을 캡처합니다."""
    screenshot = pyautogui.screenshot(region=region)
    return np.array(screenshot)

def find_template_location(screen_image, template_image):
    """스크린샷에서 템플릿 이미지의 위치를 찾습니다."""
    # 템플릿 이미지와 스크린샷을 그레이스케일로 변환
    screen_gray = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    # 템플릿 매칭 수행
    result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # 가장 높은 유사도 값을 가진 위치를 찾습니다
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 템플릿 이미지의 크기
    w, h = template_gray.shape[::-1]

    # 일치 위치에 사각형을 그립니다
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 결과를 표시합니다
    cv2.rectangle(screen_image, top_left, bottom_right, (0, 255, 0), 2)

    return top_left, bottom_right

def main():
    # 기준 이미지 파일 읽기
    template_image = cv2.imread('./Image/Lv2.png')

    # 화면 캡처 (전체 화면 또는 특정 영역)
    screen_image = capture_screen()

    # 템플릿 위치 찾기
    top_left, bottom_right = find_template_location(screen_image, template_image)

    # 좌표 출력
    print(f'Template found at: Top Left: {top_left}, Bottom Right: {bottom_right}')

    # 결과 이미지 저장 및 표시
    cv2.imwrite('result_image.png', screen_image)
    cv2.imshow('Matching Result', screen_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
