import cv2
import tensorflow as tf 

CATEGORIES = ["cloudy","foggi","raniy","sunny"]

def prepare(filepath):
    img_size = 128;
    img_array = cv2.imread(filepath);
    new_array = cv2.resize(img_array, (img_size,img_size))
    return new_array.reshape(-1,img_size,img_size,3)

model = tf.keras.models.load_model("64-CNN.model")

#prediction = model.predict([prepare('images.jpg')])
#print(CATEGORIES[int(prediction[0][0])])

def answer(path):
    img= [prepare(path)]
    prediction = model.predict(img)
    return prediction 