import cv2
import numpy as np

def red_object_tracking():

    cap = cv2.VideoCapture(0)

    cap.set(3, 1280)
    cap.set(4, 720)
    prev_center = None
    trajectory = []
    max_trajectory_length = 70
    # movement_history = []
    # max_history_length = 200

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([0, 80, 40])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 80, 40])
        upper_red2 = np.array([180, 255, 255])

        # lower_black = np.array([0, 0, 0])
        # upper_black = np.array([180, 255, 50])
        #
        # black_mask = cv2.inRange(hsv, lower_black, upper_black)
        #
        # black_only = cv2.bitwise_and(frame, frame, mask=black_mask)

        current_center = None
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        red_mask = cv2.bitwise_or(mask1, mask2) # побитовое или

        red_only = cv2.bitwise_and(frame, frame, mask=red_mask)

        kernel = np.ones((5, 5), np.uint8)
        # лучше чем квадрат kernel
        # это наш structering element
        diamond = np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]
        ], dtype=np.uint8)


        opening = cv2.dilate(cv2.erode(red_mask, diamond), diamond)
        closing = cv2.erode(cv2.dilate(opening, diamond), diamond)

        contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # _ - не используем иерархию контуров
        #CHAIN_APPROX_SIMPLE убирает лишние точки и хранит только ключевые - глы прямоугольника
        result_frame = frame.copy()

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)

            M = cv2.moments(largest_contour)
            area = M['m00'] #площадь

            if area > 1000:

                cx = int(M['m10'] / area)
                cy = int(M['m01'] / area)
                current_center = (cx, cy)

                cv2.circle(result_frame, (cx, cy), 5, (0, 255, 0), -1)  # зеленая точка

                # if prev_center is not None and current_center is not None:
                #
                #     dx = current_center[0] - prev_center[0]
                #     dy = current_center[1] - prev_center[1]
                #
                #     movement_history.append((dx, dy))
                #     if len(movement_history) > max_history_length:
                #         movement_history.pop(0)
                # prev_center = current_center

                if current_center:
                    trajectory.append(current_center)
                    if len(trajectory) > max_trajectory_length:
                        trajectory.pop(0)

                for i in range(1, len(trajectory)):
                    cv2.line(result_frame, trajectory[i - 1], trajectory[i],
                             (0, 255, 255), 2)


            else:
                # prev_center = None
                movement_info = "Object lost"
                cv2.putText(result_frame, movement_info, (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            x, y, w, h = cv2.boundingRect(largest_contour)

            #(x, y) координаты верхнего левого угла
            cv2.rectangle(result_frame, (x, y), (x + w, y + h), (0, 0, 0), 3)

            cv2.putText(result_frame, f"Area: {int(area)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        cv2.imshow('video', frame)
        cv2.imshow('Red Mask (Threshold)', red_mask)
        cv2.imshow('Red Only', red_only)
        cv2.imshow('After Opening', opening)
        cv2.imshow('After Closing', closing)
        cv2.imshow('Result with Rectangle', result_frame)


        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

red_object_tracking()