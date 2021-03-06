import cv2
import mediapipe as mp
import time

# Creating object of mediapipe
mpHands = mp.solutions.hands  # Object
mpDraw = mp.solutions.drawing_utils  # for drawing from the 21 points
hands = mpHands.Hands()

# Capturing video
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result)
    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)  # lm x,y,z values are in decimals which is the ration of h/w
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                print("id : ", id, " x,y : ",cx,cy)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)


    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



