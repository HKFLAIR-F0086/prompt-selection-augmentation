import cv2


def crop_img(img_path, x, y, w, h):
    img = cv2.imread(img_path)
    crop_img = img[208:536, 563:796]
    cv2.imwrite(img_path, crop_img)
    return crop_img


def rotate_image_clockwise(img_path):
    img = cv2.imread(img_path)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(img_path, img)
    return img


# Path: static/images/test_{n}_input.png

for i in [3, 4, 5, "x5"]:
    img_path = f"static/images/test_{i}_output.png"
    # Show the original image
    img = cv2.imread(img_path)
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cropped_img = rotate_image_clockwise(img_path)
    # Show the cropped image
    cv2.imshow("Cropped Image", cropped_img)
    cv2.waitKey(0)
