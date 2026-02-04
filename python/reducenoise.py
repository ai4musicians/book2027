# reducenoise.ipynb
%%capture
!rm -rf book2027
!git clone https://github.com/ai4musicians/book2027.git
!ls book2027/python/data
file_path = 'book2027/python/data/sinewaveC3B5.wav'
import librosa
y, sr = librosa.load(file_path)
print(f"Sampling rate (sr): {sr} Hz")
print(f"Audio data shape (y): {y.shape}")
print(f"Duration: {librosa.get_duration(y=y, sr=sr):.2f} seconds")
import numpy as np
from scipy.signal import butter, lfilter
white_noise = np.random.randn(len(y))
cutoff_freq = 8000  # Hz
normal_cutoff = cutoff_freq / (0.5 * sr)
order = 5
b, a = butter(order, normal_cutoff, btype='high', analog=False)
high_freq_noise = lfilter(b, a, white_noise)
target_amplitude = 0.2 * np.max(np.abs(y))
current_noise_amplitude = np.max(np.abs(high_freq_noise))
scaling_factor = target_amplitude / current_noise_amplitude
scaled_high_freq_noise = high_freq_noise * scaling_factor
y_noisy = y + scaled_high_freq_noise
max_amplitude_noisy = np.max(np.abs(y_noisy))
if max_amplitude_noisy > 1.0:
    y_noisy = y_noisy / max_amplitude_noisy
print("High-frequency noise generated and added to the audio signal.")
print(f"Shape of noisy audio: {y_noisy.shape}")
import numpy as np
from scipy.signal import butter, lfilter
denoisecutoff_freq = 7000  # Hz, choose a cutoff below the added noise frequency
normal_cutoff_denoise = denoisecutoff_freq / (0.5 * sr)
order_denoise = 5
b_denoise, a_denoise = butter(order_denoise, normal_cutoff_denoise, btype='low', analog=False)
y_denoised = lfilter(b_denoise, a_denoise, y_noisy)
max_amplitude_denoised = np.max(np.abs(y_denoised))
if max_amplitude_denoised > 1.0:
    y_denoised = y_denoised / max_amplitude_denoised
print("High-frequency noise removed using a low-pass filter.")
print(f"Shape of denoised audio: {y_denoised.shape}")
import matplotlib.pyplot as plt
import librosa.display
def plot_spectrogram(y, sr, title):
    plt.figure(figsize=(12, 4))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar(format='%+2.0f dB')
    plt.title(title)
    plt.tight_layout()
    plt.show()
plot_spectrogram(y, sr, 'Original Audio Spectrogram')
plot_spectrogram(y_noisy, sr, 'Noisy Audio Spectrogram')
plot_spectrogram(y_denoised, sr, 'Denoised Audio Spectrogram')
from IPython.display import Audio, display
print("Original Audio:")
display(Audio(data=y, rate=sr))
print("Noisy Audio:")
display(Audio(data=y_noisy, rate=sr))
print("Denoised Audio:")
display(Audio(data=y_denoised, rate=sr))
