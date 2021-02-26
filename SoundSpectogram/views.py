from django.shortcuts import render
from django.http import HttpResponse
import os
import librosa
import librosa.display
import IPython.display as ipd
import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64

audio_file = "audio/debussy.wav" 
audio, sr = librosa.load(audio_file)
sample_duration = 1 / sr
tot_samples = len(audio)
duration = 1 / sr * tot_samples


# Create your views here.
def SoundSpectogram(request):
    ipd.Audio(audio_file) #Play sound
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    librosa.display.waveplot(audio, alpha=0.5)
    plt.ylim((-1, 1))
    plt.title("Audio Spectrum")
    
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    
    return render(request,'SoundSpectogram.html',{'data':uri})  