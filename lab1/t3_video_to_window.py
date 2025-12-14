import cv2

cap = cv2.VideoCapture(r'C:\Users\Asus\Pictures\for_cv\WIN_20250906_10_31_16_Pro.mp4', cv2.CAP_ANY)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Размер: {width}x{height}")
print(f"FPS: {fps}")
print(f"Всего кадров: {frame_count}")

while True:
    ret, frame = cap.read() #ret - bool удалось ли выполнить чтение кадра

    if not(ret):
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('video_hsv', hsv)
    # cv2.imshow('video_gray', gray)
    # cv2.imshow('video', frame)

    # resized_down = cv2.resize(frame, (width // 10, height // 10))
    # cv2.imshow('video_sizedown_x10', resized_down)

    if cv2.waitKey(100) & 0xFF == 27: # 27 - проверяем нажата ли ESC
        break

cap.release()
cv2.destroyAllWindows()