import streamlit as st
import cv2
import mediapipe as mp

st.title("✋ Hand Gesture AI")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

while run:

    success, frame = cap.read()

    if not success:
        st.write("Camera not found")
        break

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)


    count = 0

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            lm = hand.landmark

            fingers=[4,8,12,16,20]


            # thumb
            if lm[4].x < lm[3].x:
                count+=1


            # other fingers
            for i in range(1,5):
                if lm[fingers[i]].y < lm[fingers[i]-2].y:
                    count+=1


    cv2.putText(
        frame,
        "Fingers: "+str(count),
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )


    FRAME_WINDOW.image(
        cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    )


cap.release()