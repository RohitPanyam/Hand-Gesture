# MODULE :
# class handTracker :
# 1. find_hands
#       inputs : img, draw(boolean)
#       output : returns img with the 21 point structure on it
# 2. find_posi
#       inputs : img, hand number(which had to work on), draw(boolean)
#       output : returns a list of the positions of the requested hand.


import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self, mode=False, hands_max=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.hands_max = hands_max
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpHands = mp.solutions.hands  # Object
        self.mpDraw = mp.solutions.drawing_utils  # for drawing from the 21 points
        self.hands = self.mpHands.Hands()

    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        # print(result)
        # print(result.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def find_posi(self, img, hand_number=0, draw=True):
        lm_list = []
        if self.result.multi_hand_landmarks:
            my_hand = self.result.multi_hand_landmarks[hand_number]
            for id, lm in enumerate(my_hand.landmark):
                # print(id,lm)  # lm x,y,z values are in decimals which is the ration of h/w
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print("id : ", id, " x,y : ", cx, cy)
                lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (0, 177, 225), cv2.FILLED)
        return lm_list


def main():
    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)  # width of the frame is set
    cap.set(4, hCam)  # height of the frame is set
    tracker = HandTracker()
    while True:
        success, img = cap.read()
        img = tracker.find_hands(img)
        lm_list = tracker.find_posi(img)
        if len(lm_list) != 0:
            print(lm_list[4])  # point 4 is thumb

        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
