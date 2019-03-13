import soundfile as sf
import sounddevice as sd
import time
data,sr =sf.read('weina.wav')
#sd.query_devices(device=None,kind=None)
#sd.default.device=1
sd.play(data,sr)
sd.play(data=data,samplerate=sr)
# sd.sleep(5)
time.sleep(10)
#print('sds:', sd.query_devices())
# sd.DeviceList()