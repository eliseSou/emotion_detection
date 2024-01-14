#!/usr/bin/python3
import numpy as np
import os
import soundfile
import librosa


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
