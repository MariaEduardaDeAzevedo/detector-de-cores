import cv2 as cv
import functions
import json

file = open('files/mask.json', 'r')

masks = json.load(file)

capture = cv.VideoCapture(0)

while True:
    success, frame = capture.read()
    h, w = frame.shape[:2]
    if success:
        hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        blue_mask = functions.generate_mask(masks['blue']['max'], masks['blue']['min'], hsv_image)
        yellow_mask = functions.generate_mask(masks['yellow']['max'], masks['yellow']['min'], hsv_image)
        green_mask = functions.generate_mask(masks['green']['max'], masks['green']['min'], hsv_image)

        blue_detected = cv.bitwise_and(frame, frame, mask=blue_mask)
        yellow_detected = cv.bitwise_and(frame, frame, mask=yellow_mask)
        green_detected = cv.bitwise_and(frame, frame, mask=green_mask)

        canny_blue = cv.Canny(blue_detected, 50, 50)
        canny_yellow = cv.Canny(yellow_detected, 50, 50)
        canny_green = cv.Canny(green_detected, 50, 50)
        contours_blue, hb = cv.findContours(canny_blue, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        contours_yellow, hy = cv.findContours(canny_yellow, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        contours_green, hb = cv.findContours(canny_green, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        for cnt in contours_blue:
            area = cv.contourArea(cnt)
            if area > 300:
                x, y, w, h = cv.boundingRect(cnt)
                cv.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), thickness=2)
                cv.drawContours(frame, cnt, -1, (255, 0, 0), 1)
                cv.putText(frame, "Azul", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))

        for cnt in contours_yellow:
            area = cv.contourArea(cnt)
            if area > 300:
                x, y, w, h = cv.boundingRect(cnt)
                cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,255), thickness=2)
                cv.drawContours(frame, cnt, -1, (0,255,255), 1)
                cv.putText(frame, "Amarelo", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        
        for cnt in contours_green:
            area = cv.contourArea(cnt)
            if area > 300:
                x, y, w, h = cv.boundingRect(cnt)
                cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), thickness=2)
                cv.drawContours(frame, cnt, -1, (0,255,0), 1)
                cv.putText(frame, "Verde", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))


        cv.imshow('Cam', frame)
    else:
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
