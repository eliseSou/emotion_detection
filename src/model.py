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

label_encoder = LabelEncoder()

# Removed 'calm' emotion
observed_emotions = ['neutral', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']

def load_model(dumped_model: str):
    label_encoder.fit_transform(observed_emotions)
    return keras.models.load_model(dumped_model)

def dump_model(dump_name, x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.25, random_state=42)

    # Étiquetage des émotions
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
    cnn.save(dump_name)
    return

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

def predict_emotion(model, file_name):
    print("Extracting features ...")
    x = extract_feature(file_name)
    x = np.reshape(x, (1, 180))
    print("Features extracted")
    predictions = model.predict(x)
    emotion = label_encoder.inverse_transform(predictions.argmax(axis=1))
    print("Emotion predicted : ", emotion)
    return emotion