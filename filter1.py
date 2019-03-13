import soundfile as sf
import sounddevice as sd
import time
import numpy as np
from scipy import signal

data,fs=sf.read('weina.wav')
# sd.play(data,fs)
print(fs)
b,a=signal.butter(8,0.25,'highpass')
data1=signal.filtfilt(b,a,data)
sd.play(data1,fs)
time.sleep(5)