import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy
from scipy.io import wavfile
import librosa
import librosa.display
import soundfile as sf
import sounddevice as sd

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

we =wave.open('weina.wav','rb')
for item in enumerate(we.getparams()):
    print(item)
print('********')
print(we.getframerate())
print(we.getcompname())
print(we.getnchannels())
print(we.getnframes())
print(we.getsampwidth())

print('音频时长')
print(abs(we.getnframes()/we.getframerate()))

print(we.getparams().nframes)

heng=numpy.arange(0,we.getnframes()/we.getframerate(),1/we.getframerate())
sample,squence = wavfile.read('weina.wav')
print("y######################")
print(sample)
print(squence)
plt.subplot(211)
plt.plot(heng,squence)
plt.title('波形图')
plt.xlabel("时间")
plt.subplot(212)

y,sr=librosa.load('weina.wav',sr=None)
melspec=librosa.feature.melspectrogram(y,sr,n_fft=1024,hop_length=512,n_mels=128)
logspec=librosa.power_to_db(melspec)
librosa.display.specshow(logspec,sr=sr,x_axis='time',y_axis='mel')
plt.title('pinlv')
plt.show()

print('mmmmmmmmmmmmmmm')
print(librosa.get_duration(y,sr))

y_8k=librosa.resample(y,sr,8000)
print(y.shape)
print(y_8k.shape)

print('sdgad')

plt.figure(2)
plt.subplot(211)
c=librosa.stft(y)
plt.plot(librosa.stft(y))
plt.subplot(212)
plt.plot(librosa.istft(c))
plt.show()

print('lllllllllllllllllllllll')

print(librosa.estimate_tuning(y,sr))


# # 定义数据流块
# CHUNK = 1024
# # 只读方式打开wav文件
# wf = wave.open('weina.wav', 'rb')
#
# p = pyaudio.PyAudio()
#
# # 打开数据流
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)
#
# # 读取数据
# data = wf.readframes(CHUNK)
#
# # 播放
# while data != '':
#     stream.write(data)
#     data = wf.readframes(CHUNK)
# # 停止数据流
# stream.stop_stream()
# stream.close()
# # 关闭 PyAudio
# p.terminate()