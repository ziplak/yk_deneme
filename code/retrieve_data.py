## pip install opencv-python
import cv2
import time

# reading image
image = cv2.imread("./puppy_pic.jpg")
# converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# image inversion

for tone in range(1, 10):

    inverted_image = 255 - (tone * 25) - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - (tone * 25) - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    # cv2.imshow("Original Image", image)
    file_name = f"Pencil Sketch of Dog    # Tone-{tone}"
    cv2.imshow(file_name, pencil_sketch)
    # time.sleep(1)
    # cv2.destroyWindow(file_name")
    cv2.waitKey(25559040)
