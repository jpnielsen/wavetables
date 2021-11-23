import numpy as np
import scipy.signal as scipy_signal
import scipy.io.wavfile as scipy_io_wavfile

# Settings

results = []
sampleRate = 44100                      # of samples per second (standard)
numSamples = 2048                       # of samples per waveform
numWaves   = 128                        # of waveforms in wavetable
pi         = np.pi                      # the constant pi

# Define wavetable as function of time 0 <= t < 1 
# and interpolation parameter 0 <= x < 1

def waves(t,x): 
     return scipy_signal.sawtooth(2 * pi * t, x)

# Loop through waveforms in wavetable

for waveIndex in range(numWaves):
    x = waveIndex / numWaves
    
    # Loop through samples in waveform
    for sampleIndex in range(numSamples):
        t = sampleIndex / numSamples
        
        # Append new sample to list
        results.append(waves(t,x))
         
# Generate .wav file

data = np.array(results, dtype = np.float32)
#np.savetxt("output.txt",data)
scipy_io_wavfile.write("wavetable.wav", sampleRate, data.astype('float32'))
