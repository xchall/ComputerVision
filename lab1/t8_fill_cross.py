import cv2

def fill_cross():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1200)
    cap.set(4, 920)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    center_x, center_y = w // 2, h // 2
    cross_size = 150
    thickness = 40

    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        center_pixel = frame[center_y, center_x]
        b, g, r = center_pixel
        max_val = max(r, g, b)
        if max_val == r:
            cross_color = RED
            color_name = "RED"
        elif max_val == g:
            cross_color = GREEN
            color_name = "GREEN"
        else:
            cross_color = BLUE
            color_name = "BLUE"

        # Горизонтальная полоса
        cv2.rectangle(frame,
                      (center_x - cross_size, center_y - thickness // 2),
                      (center_x + cross_size, center_y + thickness // 2),
                      cross_color, -1)

        # Вертикальная полоса
        cv2.rectangle(frame,
                      (center_x - thickness // 2, center_y - cross_size),
                      (center_x + thickness // 2, center_y - thickness // 2),
                      cross_color, -1)

        cv2.rectangle(frame,
                      (center_x - thickness // 2, center_y + thickness // 2),
                      (center_x + thickness // 2, center_y + cross_size),
                      cross_color, -1)

        cv2.putText(frame, f"Center RGB: ({r},{g},{b})", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, f"Cross color: {color_name}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

fill_cross()