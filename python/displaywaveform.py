# displaywaveform.py
!rm -rf book2027
!git clone https://github.com/ai4musicians/book2027.git
!ls -R book2027
!pip install -q librosa soundfile matplotlib
import librosa
import librosa.display
import matplotlib.pyplot as plt
import IPython.display as ipd
file_path = 'book2027/python/data/music01.mp3'
y, sr = librosa.load(file_path)
ipd.Audio(file_path)
plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform of music01.mp3')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
