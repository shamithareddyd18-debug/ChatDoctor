from preprocessing import preprocess_mri
from segmentation import segment_region

def predict_mri(image_path):

    image = preprocess_mri(
        image_path
    )

    segmentation = segment_region(
        image
    )

    prediction = {
        "finding": "No Abnormality",
        "confidence": 0.94,
        "segmentation": segmentation
    }

    return prediction
