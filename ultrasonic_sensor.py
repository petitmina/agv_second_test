import RPi.GPIO as GPIO
import time

# 초음파 센서 핀 설정
TRIG_PIN = 23  # Trig 핀
ECHO_PIN = 24  # Echo 핀

# GPIO 핀 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# 초음파 센서로 거리 측정
def get_distance():
    # Trig 핀에 신호를 10μs 동안 HIGH로 설정
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10μs 대기
    GPIO.output(TRIG_PIN, False)

    # Echo 핀에서 신호가 돌아오는 시간 측정
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    # 신호가 왕복하는 데 걸린 시간
    elapsed_time = stop_time - start_time

    # 초음파의 속도 (34300 cm/s)로 거리 계산
    distance = (elapsed_time * 34300) / 2  # 거리 (cm)

    return distance

# 장애물이 일정 거리 이내에 있는지 확인
def is_obstacle_nearby(threshold_distance=30):
    distance = get_distance()
    if distance < threshold_distance:
        print(f"Obstacle detected! Distance: {distance} cm")
        return True
    else:
        print(f"Clear path. Distance: {distance} cm")
        return False
