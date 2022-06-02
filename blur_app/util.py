import cv2


def get_blurred_face_image(image):
    # get height and width from image
    height, width = image.shape[:2]

    cascade_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face = cascade_model.detectMultiScale(gray_image,
                                          scaleFactor=1.3,
                                          minNeighbors=5)

    for x, y, w, h in face:
        image = cv2.rectangle(image, (x, y),
                              (x + w, y + h),
                              (0, 255, 0), 3)

        image[y:y + h, x:x + w] = cv2.medianBlur(image[y:y + h, x:x + w],
                                                 35)

    return image


