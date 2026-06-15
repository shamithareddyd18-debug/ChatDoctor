import cv2

def preprocess_xray(path):

    image = cv2.imread(path)

    image = cv2.resize(
        image,
        (224,224)
    )

    return image
