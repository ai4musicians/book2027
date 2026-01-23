# playmp3.py
!rm -rf book2027
!git clone https://github.com/ai4musicians/book2027.git
!ls book2027/python/data
from IPython.display import Image, display
import os
image_file_path = os.path.join('book2027', 'python', 'data', 'music01.png')
display(Image(filename=image_file_path))
import ipywidgets as widgets
from IPython.display import display, Audio
import os
mp3_file_path = os.path.join('book2027', 'python', 'data', 'music01.mp3')
play_mp3_button = widgets.Button(
    description='Play music01.mp3',
    disabled=False,
    button_style='info', # A different style for distinction
    tooltip='Click to play music01.mp3',
    icon='play'
)
def on_mp3_button_clicked(b):
    print(f"Playing {mp3_file_path}...")
    display(Audio(mp3_file_path, autoplay=True))
play_mp3_button.on_click(on_mp3_button_clicked)
display(play_mp3_button)
