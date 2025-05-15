import numpy as np
from tensorflow.keras.applications.mobilenet import MobileNet, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

# Load the pre-trained MobileNet model
model = MobileNet(weights="imagenet")

def predict_image(image):
    # Preprocess image
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    # Predict
    preds = model.predict(image)
    decoded = decode_predictions(preds, top=1)[0][0]
    return f"{decoded[1]} ({decoded[2]*100:.2f}%)"

