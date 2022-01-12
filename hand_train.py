import cv2
import time
import mediapipe as mp
cap = cv2.VideoCapture(0)
mphand = mp.solutions.hands
hand = mphand.Hands()
mpdraw = mp.solutions.drawing_utils
mp_face_draw = mp.solutions.drawing_styles
mpface = mp.solutions.face_mesh
face_mesh = mpface.FaceMesh(static_image_mode=True)

while True:
    ret, img = cap.read()
    imgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hand.process(imgr)
    resultface = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    #result.multi_hand_landmarks

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(img, handlms, mphand.HAND_CONNECTIONS)
            sum1 = 0
            for id, lm in enumerate(handlms.landmark):

                h, w, c = img.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id==4:
                    c4x = cx
                    c4y = cy
                    cv2.circle(img, (cx, cy), 10,(255,0,255),cv2.FILLED )
                    if cy<229:
                        sum1=sum1+1
                if id==8:
                    c8x = cx
                    c8y = cy
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                    cv2.line(img, (c4x, c4y), (c8x, c8y), (69, 255, 0), 3)
                    if cy<200:
                        sum1=sum1+1
                if id==12:
                    cv2.line(img, (c4x, c4y), (cx, cy), (69, 255, 0), 3)
                    if cy<200:
                        sum1=sum1+1
                if id == 16:
                    cv2.line(img, (c4x, c4y), (cx, cy), (69, 255, 0), 3)
                    if cy<200:
                        sum1=sum1+1
                if id == 20:
                    cv2.line(img, (c4x, c4y), (cx, cy), (69, 255, 0), 3)
                    if cy<200:
                        sum1=sum1+1

                    cv2.putText(img,str(sum1),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    for face_landmarks in resultface.multi_face_landmarks:
        mpdraw.draw_landmarks(img,face_landmarks,mpface.FACEMESH_FACE_OVAL, landmark_drawing_spec=mpdraw.DrawingSpec(circle_radius=1,color=(0,255,255)))




    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()