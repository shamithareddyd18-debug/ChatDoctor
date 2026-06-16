from ChatDoctor_MRI.inference import (
    predict_mri
)

result = predict_mri(
    "sample_images/brain_mri.jpg"
)

print(result)
