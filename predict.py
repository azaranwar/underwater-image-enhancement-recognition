import tensorflow as tf
from PIL import Image
import numpy as np

class ImagePredictor:
    def __init__(self, model_path):
        # Load the trained model
        self.model = tf.keras.models.load_model(model_path)

    def preprocess_image(self, image_path):
        # Load an image and preprocess it for prediction
        image = Image.open(image_path)
        image = image.resize((224, 224))  # Adjust size as needed
        image_array = np.array(image) / 255.0  # Normalize if required
        return np.expand_dims(image_array, axis=0)  # Add batch dimension

    def predict_single(self, image_path):
        # Make a prediction for a single image
        preprocessed_image = self.preprocess_image(image_path)
        predictions = self.model.predict(preprocessed_image)
        return predictions

    def predict_batch(self, image_paths):
        # Make predictions for a batch of images
        images = np.vstack([self.preprocess_image(img) for img in image_paths])
        predictions = self.model.predict(images)
        return predictions
