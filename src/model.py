#!/usr/bin/python3

import numpy as np
import os
import soundfile
import librosa
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tqdm.notebook import tqdm_notebook
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from sklearn import svm
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import keras

emotions = {
    '01': "neutral", 
    '02': "calm", 
    '03': "happy", 
    '04': "sad", 
    '05': "angry", 
    '06': "fearful", 
    '07': "disgust", 
    '08': "surprised"
}

# Removed 'calm' emotion
observed_emotions = ['neutral', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']

ravdess_folder = "./data_samples/RAVDESS"
excluded_files = ["README.md","03-01-06-01-01-02-20.wav", "03-01-08-01-02-02-01.wav", "03-01-03-01-02-01-20.wav"]

def load_data(folder_path, emotions, excluded_files=[], test_size=0.2):
    x,y = [],[]
    files = os.listdir(folder_path)
    
    # iterations with the progress bar
    for i in tqdm_notebook(range(len(files)-len(excluded_files))):
        file = files[i]
        
        if file not in excluded_files:
            file_name = os.path.basename(file)
            emotion = emotions[file_name.split("-")[2]]

            if emotion not in observed_emotions:
                continue

            feature = extract_feature(folder_path + "/" + file)

            x.append(feature)
            y.append(emotion)
    return np.array(x), np.array(y)

def extract_feature(file_name, mfcc=True, chroma=True, mel=True):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")

        sample_rate = sound_file.samplerate

        if chroma:
            stft = np.abs(librosa.stft(X))
        result=np.array([])

        # MFCC Criterias (short-term power spectrum of a sound)
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))

        # Pertains to the 12 diffrent pitch classes
        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result = np.hstack((result, chroma))
        
        # MEL Spectrogram Frequency
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T,axis=0)
            result = np.hstack((result, mel))
    return result

x,y = load_data(ravdess_folder, emotions=emotions, excluded_files=excluded_files)
x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.25, random_state=42)

# Étiquetage des émotions
label_encoder = LabelEncoder()
y_cnn = label_encoder.fit_transform(y)
y_cnn = to_categorical(y_cnn, num_classes=len(label_encoder.classes_))

x_train, x_test, y_train, y_test = train_test_split(x, y_cnn, test_size=0.2, random_state=42)

# Création du modèle CNN
cnn = models.Sequential()
cnn.add(layers.Reshape((180, 1), input_shape=(180,)))  # Reshape pour ajouter la dimension du canal
cnn.add(layers.Conv1D(32, 3, activation='relu'))
cnn.add(layers.MaxPooling1D(2))
cnn.add(layers.Conv1D(64, 3, activation='relu'))
cnn.add(layers.MaxPooling1D(2))
cnn.add(layers.Conv1D(128, 3, activation='relu'))
cnn.add(layers.MaxPooling1D(2))
cnn.add(layers.Flatten())
cnn.add(layers.Dense(128, activation='relu'))
cnn.add(layers.Dense(len(label_encoder.classes_), activation='softmax'))

# Compilation du modèle
cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
cnn.fit(x_train, y_train, epochs=50, batch_size=32, validation_data=(x_test, y_test))

# Évaluation du modèle
test_loss, test_acc = cnn.evaluate(x_test, y_test)
print(f'Test Accuracy: {test_acc}')


# Calling `save('my_model.keras')` creates a zip archive `my_model.keras`.
cnn.save("my_model.cnn")

# It can be used to reconstruct the model identically.
reconstructed_model = keras.models.load_model("my_model.cnn")

# Let's check:
np.testing.assert_allclose(
    cnn.predict(x_train), reconstructed_model.predict(x_train)
)