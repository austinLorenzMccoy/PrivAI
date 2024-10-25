#model.py
import tensorflow as tf
from tensorflow.keras import layers, models

class LoRALayer(layers.Layer):
    def __init__(self, original_layer, rank=4, **kwargs):
        super().__init__(**kwargs)
        self.original_layer = original_layer
        self.rank = rank

    def build(self, input_shape):
        self.lora_A = self.add_weight(shape=(self.original_layer.kernel.shape[0], self.rank),
                                      initializer='random_normal', trainable=True)
        self.lora_B = self.add_weight(shape=(self.rank, self.original_layer.kernel.shape[1]),
                                      initializer='random_normal', trainable=True)

    def call(self, inputs):
        return self.original_layer(inputs) + tf.matmul(tf.matmul(inputs, self.lora_A), self.lora_B)

def build_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    return model
