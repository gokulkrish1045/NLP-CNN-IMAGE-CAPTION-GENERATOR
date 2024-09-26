import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_images(image_folder):
    images = []
    for filename in os.listdir(image_folder):
        img = load_img(os.path.join(image_folder, filename), target_size=(224, 224))  # Example size
        img = img_to_array(img) / 255.0  # Normalize image
        images.append(img)
    return np.array(images)

def load_captions(captions_file):
    with open(captions_file, 'r') as f:
        captions = f.readlines()
    return [caption.strip() for caption in captions]

def tokenize_captions(captions):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(captions)
    return tokenizer
