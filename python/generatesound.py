# generatesound.ipynb
def calculate_frequency(note):
  # 49 is A4, 440 Hz
  return 440 * (2 ** ((note - 49) / 12))
import numpy as np
def generate_sine_wave(frequency, duration, sampling_rate):
  t = np.linspace(0., duration, int(sampling_rate * duration), endpoint=False)
  audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
  # Scale to 16-bit integer format (standard for WAV files)
  audio_data = (audio_data * 32767).astype(np.int16)
  return audio_data
C3 = 38
B5 = 63
all_notes = []
duration = 1    # seconds
sampling_rate = 44100 # samples per second (standard audio CD quality)
for note in range(C3, B5 + 1):
  frequency = calculate_frequency(note)
  audio_data = generate_sine_wave(frequency, duration, sampling_rate)
  all_notes.append(audio_data)
# convert a Python list to a numpy array
combined_notes_audio = np.concatenate(all_notes)
from IPython.display import Audio
Audio(combined_notes_audio, rate=sampling_rate, autoplay=False)
# Audio(all_notes, rate=sampling_rate, autoplay=False)
from scipy.io import wavfile
output_filename = 'sinewave.wav'
wavfile.write(output_filename, sampling_rate, audio_data)
print(f"save audio file '{output_filename}'.")
