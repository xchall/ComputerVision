import cv2

def read_write_file(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Four Character Code - каким образом сжимаем/кодируем видео при записи
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # альтернативный код для записи в AVI
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (w, h))
    while (True):
        ret, frame = cap.read()

        if not (ret):
            break

        cv2.imshow('video', frame)
        video_writer.write(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

input_path = r'C:\Users\Asus\Pictures\for_cv\WIN_20250906_10_31_16_Pro.mp4'
# output_path = r'C:\Users\Asus\Pictures\for_cv\output.mp4'
output_path = r'C:\Users\Asus\Pictures\for_cv\output.avi'
read_write_file(input_path, output_path)