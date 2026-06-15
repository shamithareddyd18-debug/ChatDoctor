import cv2

def preprocess_mri(image_path):

    image = cv2.imread(image_path)

    image = cv2.resize(
        image,
        (256, 256)
    )

    image = image / 255.0

    return image
