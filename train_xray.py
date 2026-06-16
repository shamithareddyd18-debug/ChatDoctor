from ChatDoctor_XRay.inference import (
    predict_xray
)

result = predict_xray(
    "sample_images/normal_xray.jpg"
)

print(result)
