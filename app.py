import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("rice_classifier_mobilenetv2.h5")

# Class labels
class_labels = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

# App title
st.title("🌾 Rice Grain Classifier")
st.markdown("Upload a rice grain image and see the predicted type.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_data = Image.open(uploaded_file)
    st.image(image_data, caption='Uploaded Image', use_container_width=True)


    # Preprocess image
    img = image_data.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]

    # Display result
    st.success(f"✅ Predicted Rice Type: **{predicted_class}**")
