import cv2

img = cv2.imread(r'C:\Users\Asus\Pictures\for_cv\statue.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'C:\Users\Asus\Pictures\for_cv\white_fox.webp', cv2.IMREAD_COLOR)
img3 = cv2.imread(r'C:\Users\Asus\Pictures\for_cv\dancing_man.gif', cv2.IMREAD_REDUCED_COLOR_2)

cv2.namedWindow('output', cv2.WINDOW_NORMAL)
cv2.imshow('output', img)
cv2.waitKey(2000)

cv2.namedWindow('output2', cv2.WINDOW_AUTOSIZE)
cv2.imshow('output2', img2)
cv2.waitKey(2000)

cv2.namedWindow('output3', cv2.WINDOW_FULLSCREEN)
cv2.imshow('output3', img3)
cv2.waitKey(0)