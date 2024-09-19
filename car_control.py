import RPi.GPIO as GPIO

#pull수정
# GPIO 핀 설정
left_motor_pin = 17
right_motor_pin = 18
backward_left_motor_pin = 22  # 후진을 위한 추가 핀 설정 (예시)
backward_right_motor_pin = 23  # 후진을 위한 추가 핀 설정 (예시)

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_pin, GPIO.OUT)
GPIO.setup(right_motor_pin, GPIO.OUT)
GPIO.setup(backward_left_motor_pin, GPIO.OUT)
GPIO.setup(backward_right_motor_pin, GPIO.OUT)

def go_left():
    GPIO.output(left_motor_pin, GPIO.HIGH)
    GPIO.output(right_motor_pin, GPIO.LOW)
    GPIO.output(backward_left_motor_pin, GPIO.LOW)
    GPIO.output(backward_right_motor_pin, GPIO.LOW)
    print("Turning Left")
    
def go_right():
    GPIO.output(left_motor_pin, GPIO.LOW)
    GPIO.output(right_motor_pin, GPIO.HIGH)
    GPIO.output(backward_left_motor_pin, GPIO.LOW)
    GPIO.output(backward_right_motor_pin, GPIO.LOW)
    print("Turning Right")

def go_straight():
    GPIO.output(left_motor_pin, GPIO.HIGH)
    GPIO.output(right_motor_pin, GPIO.HIGH)
    GPIO.output(backward_left_motor_pin, GPIO.LOW)
    GPIO.output(backward_right_motor_pin, GPIO.LOW)
    print("Going Straight")

def go_backward():
    GPIO.output(left_motor_pin, GPIO.LOW)
    GPIO.output(right_motor_pin, GPIO.LOW)
    GPIO.output(backward_left_motor_pin, GPIO.HIGH)
    GPIO.output(backward_right_motor_pin, GPIO.HIGH)
    print("Going Backward")

def go_slow():
    # 천천히 멈출 준비 (예시로 LOW 속도를 설정)
    GPIO.output(left_motor_pin, GPIO.HIGH)
    GPIO.output(right_motor_pin, GPIO.HIGH)
    print("Slowing down, preparing to stop")

def stop():
    GPIO.output(left_motor_pin, GPIO.LOW)
    GPIO.output(right_motor_pin, GPIO.LOW)
    GPIO.output(backward_left_motor_pin, GPIO.LOW)
    GPIO.output(backward_right_motor_pin, GPIO.LOW)
    print("Stopping")

def control_car(lane_center, frame_width, person_detected, traffic_light_color, obstacle_nearby):
    if person_detected:
        print("Person detected, stopping the car.")
        stop()  # 사람이 감지되면 멈춤
        return

    if traffic_light_color == "red":
        print("Red traffic light detected, stopping the car.")
        stop()  # 빨간 신호등이 감지되면 멈춤
        return
    
    if traffic_light_color == "yellow":
        print("Yellow traffic light detected, slowing down.")
        go_slow()  # 노란 신호등이 감지되면 속도를 줄임 (멈출 준비)
        return

    if obstacle_nearby:
        print("Obstacle detected, stopping the car.")
        stop()  # 장애물이 있으면 멈춤
        return

    frame_center = frame_width // 2
    threshold = 30

    if lane_center is not None:
        if lane_center < frame_center - threshold:
            go_left()
        elif lane_center > frame_center + threshold:
            go_right()
        else:
            go_straight()
    else:
        go_backward()