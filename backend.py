import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator


#progress tracking library
import wandb
from wandb.keras import WandbCallback
wandb.login()

#code logging
run = wandb.init(project="last-weather-recognization")
config = run.config
config.epochs= 60
config.size = 128
config.dropout= 0.3
config.batch_size= 14
config.pool_size=(6,6)
config.shear_range= 0.4
config.zoom_range=0.4


#initializing cnn
classifier = Sequential()
    
#Convolution
size= config.size
classifier.add(Conv2D(64,3,3, input_shape= (size,size,3), activation= 'relu'))
    

 
#second layer
classifier.add(Conv2D(64,3,3, activation= 'relu'))
classifier.add(MaxPooling2D(pool_size=config.pool_size))
 

classifier.add(Dropout(rate= config.dropout ))   
#flattening
classifier.add(Flatten())

# input layer
classifier.add(Dense(size, activation ='relu' ))   

#first hidden layer
classifier.add(Dense(size, activation ='relu' ))
classifier.add(Dropout(rate= config.dropout ))



classifier.add(Dense(units = 4, activation = 'softmax'))

# Compiling the CNN
classifier.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'] )

# Part 2 - Fitting the CNN to the images
#augumentation 
batch = config.batch_size
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator


train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=config.shear_range,
            zoom_range=config.zoom_range,
            horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(directory=r'dynamic_dataset',
                                                    target_size=(size, size),
                                                    batch_size=batch,
                                                    class_mode="categorical")


test_set = test_datagen.flow_from_directory(directory=r'dynamic_dataset',
                                                target_size=(size, size),
                                                batch_size=batch,
                                                class_mode="categorical")


labels = ["cloud","foggy","raniy","sunny"]


classifier.fit(training_set,
                steps_per_epoch = 1203/batch,
                epochs=config.epochs,
                validation_data=test_set,
                validation_steps = 84/batch
                )

wandb.finish()

classifier.save("64-CNN.model")

