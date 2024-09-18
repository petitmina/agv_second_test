import cv2
from lane_detection import detect_lanes
from car_control import control_car, stop
from person_detection import detect_person
from traffic_light_detection import detect_traffic_light
from ultrasonic_sensor import is_obstacle_nearby
import RPi.GPIO as GPIO

def process_video():
    cap = cv2.VideoCapture(0)  # 카메라 연결

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # 사람 인식
        person_detected = detect_person(frame)

        # 차선 감지
        lanes_image, lane_center = detect_lanes(frame)

        # 신호등 인식
        traffic_light_color = detect_traffic_light(frame) 

        # 초음파 센서로 장애물 감지
        obstacle_nearby = is_obstacle_nearby()

        # 자동차 방향 제어
        control_car(lane_center, frame.shape[1], person_detected, traffic_light_color, obstacle_nearby)

        # 결과 화면에 출력
        cv2.imshow('Lane Detection', lanes_image)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        process_video()
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
