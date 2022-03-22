import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

MODEL_FILE_PATH = "./scamphotoapp/ml.models/model.h5"
image_size = 64
females = ["美白加工系詐欺女性", "マスク詐欺女性", "SNOW詐欺女性", "角度詐欺女性", "一般女性"]
classes = ["purikura", "mask", "snow", "degree", "normal"]


# 予測する関数
def predict(face_image):
    model = load_model(MODEL_FILE_PATH)
    
    image = load_img(face_image)
    image = image.resize((image_size, image_size))
    image = img_to_array(image)

    data  = np.array(image) / 255.0
    data  = np.expand_dims(data, axis=0)

    result = model.predict([data])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)

    return (females[predicted], classes[predicted], percentage)