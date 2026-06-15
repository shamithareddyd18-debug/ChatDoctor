from preprocessing import preprocess_xray

def predict_xray(image_path):

    image = preprocess_xray(
        image_path
    )

    result = {
        "finding": "Normal",
        "confidence": 0.95
    }

    return result
