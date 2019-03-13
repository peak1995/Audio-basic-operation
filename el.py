import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import sounddevice

y,sr=librosa.load('weina.wav',sr=None)
plt.figure()
D=librosa.amplitude_to_db(librosa.stft(y),ref=np.max)

librosa.display.specshow(D,y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Linear-frequency power spectrogram')
plt.show()