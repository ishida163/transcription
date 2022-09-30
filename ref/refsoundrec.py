import sounddevice as sd
import soundfile as sf
import numpy as np

duration = 10  # 10秒間録音する

# デバイス情報関連
sd.default.device = [8, 8] # Input, Outputデバイス指定 --現状ステレオミキサー
input_device_info = sd.query_devices(device=sd.default.device[1])
sr_in = int(input_device_info["default_samplerate"])

# 録音
myrecording = sd.rec(int(duration * sr_in), samplerate=sr_in, channels=2)
sd.wait() # 録音終了待ち

print(myrecording.shape) #=> (duration * sr_in, channels)

# 録音信号のNumPy配列をwav形式で保存
sf.write("./myrecording.wav", myrecording, sr_in)