import cv2
import Hand_tracking_mod as htm



cap = cv2.VideoCapture(0)
wCam ,hCam = 640,480
cap.set(3,wCam)   # width of the frame is set
cap.set(4,hCam )  # height of the frame is set

tracker = htm.HandTracker()

finger_pts = [4,8,12,16,20] #
fingers = ["Thumb","Index","Middle","Ring","Little"]

while True:
    suc,img = cap.read()
    img = tracker.find_hands(img)
    pts = tracker.find_posi(img,draw=False) #points of the hand
    # print(pts) # pt,(w,h)  --> pt,(x,y)
    if len(pts)!=0:
        # print(pts[8])
        # print(pts[6])
        # print(pts[4])
        # print(pts[2])
        open = []
        if pts[4][1] > pts[3][1]:
            open.append(1)
        else:
            open.append(0)
        for pt in finger_pts[1:]:
            if pts[pt][2]<pts[pt-2][2]:
                open.append(1)
            else:
                open.append(0)
                # print(pt)
                # print("{} is up".format(fingers[int(pt/4)]))
        print(open)

    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
