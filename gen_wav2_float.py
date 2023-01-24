import numpy as np
import scipy.io.wavfile as scipy_io_wavfile
from scipy import signal

# Settings
sampleRate = 44100  # of samples per second (standard)
numSamples = 2048  # of samples per waveform
numWaves = 128  # of waveforms in wavetable
pi = np.pi  # the constant pi

# Define wavetable as function of time 0 <= t < 1
# and sawtooth maximum parameter 0 <= x < 1

def waves(t, x):
    return signal.sawtooth(2 * pi * t, x)

# Loop through waveforms in wavetable
x = np.linspace(0, 1, numWaves)
t = np.linspace(0, 1, numSamples)

# Loop through samples in waveform
data = np.empty(0, dtype=np.float32)  # empty float32 array
for waveIndex in range(numWaves):
    data = np.append(data, waves(t, x[waveIndex]))

# Generate .wav file

scipy_io_wavfile.write("wavetable.wav", sampleRate, data.astype('float32'))
