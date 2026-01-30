# analyzefrequencies.py
%%capture
!rm -rf book2027
!git clone https://github.com/ai4musicians/book2027.git
!ls book2027/python/data
file_path = 'book2027/python/data/sinewaveC3B5.wav'
from scipy.io import wavfile
sampling_rate, audio_samples = wavfile.read(file_path)
num_segments = len(audio_samples) // sampling_rate
audio_segments = []
for i in range(num_segments):
    start_index = i * sampling_rate
    end_index = start_index + sampling_rate
    segment = audio_samples[start_index:end_index]
    audio_segments.append(segment)
print(f"Number of segments created: {len(audio_segments)}")
print(f"Length of the first segment: {len(audio_segments[0])} samples")
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import windows
dominant_frequencies_per_segment = []
for segment in audio_segments:
    window = windows.hann(len(segment))
    windowed_segment = segment * window
    yf = fft(windowed_segment)
    magnitude = np.abs(yf)
    xf = fftfreq(len(segment), 1 / sampling_rate)
    positive_frequencies = xf[:len(segment) // 2]
    positive_magnitudes = magnitude[:len(segment) // 2]
    max_magnitude_index = np.argmax(positive_magnitudes)
    dominant_frequency = positive_frequencies[max_magnitude_index]
    dominant_frequencies_per_segment.append(dominant_frequency)
for i, freq in enumerate(dominant_frequencies_per_segment):
    print(f"Segment {i+1:2}: {freq:.2f} Hz")
