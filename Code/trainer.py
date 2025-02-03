import os
import librosa
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models

# Constants
DATA_DIR = "final_name/"  # Directory containing MP3/WAV files
TARGET_WORD = "stanley"
SAMPLE_RATE = 16000
MFCC_FEATURES = 40
MAX_LENGTH = 100  # Adjust based on typical length of "Stanley"

# Function to extract MFCC features
def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=SAMPLE_RATE)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=MFCC_FEATURES)
    mfcc = np.pad(mfcc, ((0, 0), (0, max(0, MAX_LENGTH - mfcc.shape[1]))), mode='constant')
    return mfcc[:, :MAX_LENGTH]

# Load dataset
def load_dataset():
    X, y = [], []
    for label, folder in enumerate(["positive", "negative"]):
        folder_path = os.path.join(DATA_DIR, folder)
        for file in os.listdir(folder_path):
            if file.endswith(".mp3") or file.endswith(".wav"):
                file_path = os.path.join(folder_path, file)
                features = extract_features(file_path)
                X.append(features)
                y.append(label)
    return np.array(X), np.array(y)

# Load and preprocess data
X, y = load_dataset()
X = X[..., np.newaxis]  # Add channel dimension for CNN
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build CNN model
def build_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(MFCC_FEATURES, MAX_LENGTH, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Binary classification
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Train the model
model = build_model()
history = model.fit(X_train, y_train, epochs=20, batch_size=16, validation_data=(X_test, y_test))

# Save model
model.save("wake_word_model.h5")

# Plot training results
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
