import numpy as np
import math
import cv2


def gaussian_function(x, y, sigma): # передаем сразу с минус центрами
    return (1 / (2 * np.pi * sigma ** 2)) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

def normalize_kernel(kernel):
    return kernel / np.sum(kernel)

def Gauss_filter(image, ker):
    height, width = image.shape
    pad = kernel_size // 2
    res_matrix = image.copy()

    print("Высота и ширина изображения:", height, width)

    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            region = image[i - pad:i + pad + 1, j - pad:j + pad + 1]
            res_matrix[i, j] = np.sum(region * ker)

    print(res_matrix)

    return res_matrix



sigma = 1.0
kernel_size = 3
center = math.ceil(kernel_size / 2) - 1
print(center)

gaussian_matrix = np.zeros((kernel_size, kernel_size))
for i in range(kernel_size):
    for j in range(kernel_size):
        x = j - center
        y = i - center
        gaussian_matrix[i, j] = gaussian_function(x, y, sigma)

print("Матрица Гаусса до нормировки:")
print(gaussian_matrix)

print(f"Сумма элементов: {np.sum(gaussian_matrix):.6f}")
normalized_matrix = normalize_kernel(gaussian_matrix)

print("\nМатрица Гаусса после нормировки:")
print(normalized_matrix)

print(f"Сумма элементов: {np.sum(normalized_matrix):.6f}")


img = cv2.imread(r'C:\Users\Asus\Pictures\for_cv\kanye_west.jpg', cv2.IMREAD_GRAYSCALE)


print(img)
cv2.imshow("original_img", img)
cv2.waitKey(1000)

img_after_hand_blur = Gauss_filter(img, normalized_matrix)

cv2.imshow("img_after_hand_blur", img_after_hand_blur)
cv2.waitKey(1000)

blurred = cv2.GaussianBlur(img, (11, 11), 3.0)
cv2.imshow("img_after_cv_blur", blurred)
cv2.waitKey(0)
