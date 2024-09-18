import cv2

# 사람 인식 함수 (Haar Cascade 사용)
def detect_person(frame):
    # Haar Cascade 모델 로드
    person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    people = person_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    
    if len(people) > 0:
        for (x, y, w, h) in people:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return True  # 사람이 있을 때
    return False  # 사람이 없을 때
