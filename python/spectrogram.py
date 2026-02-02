# spectrogram.ipynb
%%capture
!rm -rf book2027
!git clone https://github.com/ai4musicians/book2027.git
!ls book2027/python/data
%%capture
!pip install librosa soundfile matplotlib
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
audio_file = 'book2027/python/data/sinewaveC3B5.wav'
y, sr = librosa.load(audio_file)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='linear') # Changed y_axis to 'linear'
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram of sinewaveC3B5.wav')
plt.ylim(100, 1000) # Set y-axis limits between 100 Hz and 1000 Hz
plt.tight_layout()
plt.show()
