import cv2

def print_cam():
    cap = cv2.VideoCapture(0)

    cap.set(3, 1200)
    cap.set(4, 920)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    center_x, center_y = w // 2, h // 2
    cross_size = 150
    thickness = 40

    while True:
        ret, frame = cap.read()

        if not (ret):
            break

        h_start_y = center_y - thickness // 2
        h_end_y = center_y + thickness // 2
        h_start_x = center_x - cross_size
        h_end_x = center_x + cross_size
        horizontal_region = frame[h_start_y:h_end_y, h_start_x:h_end_x] #region of interest
        blurred_horizontal = cv2.blur(horizontal_region, (25, 25))
        frame[h_start_y:h_end_y, h_start_x:h_end_x] = blurred_horizontal

        # Горизонтальная полоса
        cv2.rectangle(frame,
                      (center_x - cross_size, center_y - thickness // 2),
                      (center_x + cross_size, center_y + thickness // 2),
                      (0, 0, 255), 0) # 0 - толщина рамки в 1 пиксель

        # Вертикальная полоса
        cv2.rectangle(frame,
                      (center_x - thickness // 2, center_y - cross_size),
                      (center_x + thickness // 2, center_y - thickness // 2),
                      (0, 0, 255), 0)

        cv2.rectangle(frame,
                      (center_x - thickness // 2, center_y + thickness // 2),
                      (center_x + thickness // 2, center_y + cross_size),
                      (0, 0, 255), 0)


        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break


    cap.release()
    cv2.destroyAllWindows()

print_cam()