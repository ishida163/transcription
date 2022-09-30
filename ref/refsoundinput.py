import sounddevice as sd
import numpy as np
duration = 10  # 10秒間収音する

sd.default.device = [8, 8] # Input, Outputデバイス指定

def callback(indata, frames, time, status):
    # indata.shape=(n_samples, n_channels)
    # print root mean square in the current frame
    print(np.sqrt(np.mean(indata**2)))

with sd.InputStream(
        channels=1, 
        dtype='float32', 
        callback=callback
    ):
    sd.sleep(int(duration * 1000))