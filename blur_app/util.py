import cv2


def get_blurred_face_image(image):
    # get height and width from image
    height, width = image.shape[:2]


    cascade_model = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cords = cascade_model.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1)

    for x, y, w, h in face_cords:
        blur_face = image[y:y + h, x:x + w]
        blur_face = cv2.GaussianBlur(blur_face, (23, 23), 30)
        image[y:y + blur_face.shape[0], x:x + blur_face.shape[1]] = blur_face

    return image


