import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Input, concatenate

def unet_model(input_size=(256, 256, 1)):
    inputs = Input(input_size)
    conv1 = Conv2D(64, (3,3), activation='relu', padding='same')(inputs)
    conv1 = Conv2D(64, (3,3), activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2,2))(conv1)

    conv2 = Conv2D(128, (3,3), activation='relu', padding='same')(pool1)
    conv2 = Conv2D(128, (3,3), activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=(2,2))(conv2)

    up1 = UpSampling2D(size=(2,2))(pool2)
    merge1 = concatenate([conv1, up1], axis=-1)
    conv3 = Conv2D(64, (3,3), activation='relu', padding='same')(merge1)
    conv3 = Conv2D(64, (3,3), activation='relu', padding='same')(conv3)

    output = Conv2D(1, (1,1), activation='sigmoid')(conv3)

    model = Model(inputs, output)
    return model

if __name__ == "__main__":
    model = unet_model()
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    print("✅ U-Net Model Created for Pipe Removal")
