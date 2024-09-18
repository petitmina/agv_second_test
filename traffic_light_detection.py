import cv2
import numpy as np

def detect_traffic_light(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 빨간색 마스크
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_frame, red_lower, red_upper)

    # 녹색 마스크
    green_lower = np.array([40, 50, 50])
    green_upper = np.array([90, 255, 255])
    green_mask = cv2.inRange(hsv_frame, green_lower, green_upper)

    # 노란색 마스크
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, yellow_lower, yellow_upper)

    # 빨간색 신호등 감지
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(red_contours) > 0:
        return "red"  # 빨간 신호등 감지

    # 녹색 신호등 감지
    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(green_contours) > 0:
        return "green"  # 녹색 신호등 감지

    # 노란색 신호등 감지
    yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(yellow_contours) > 0:
        return "yellow"  # 노란 신호등 감지

    return "none"  # 신호등 없음
