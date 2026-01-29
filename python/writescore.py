# writescore.py
# %%capture
# import music21
# !apt-get update
# !apt-get install musescore3
import music21
def list2score(notes: list, type = "eighth"):
    score = music21.stream.Score()
    treble_part = music21.stream.Part()
    treble_part.append(music21.clef.TrebleClef())
    bass_part = music21.stream.Part()
    bass_part.append(music21.clef.BassClef())
    middle_c_pitch = music21.note.Note('C4').pitch
    for x in notes:
      n = music21.note.Note(x)
      n.duration.type = type
      if n.pitch < middle_c_pitch:
        bass_part.append(n)
        treble_part.append(music21.note.Rest(duration=n.duration))
      else:
        treble_part.append(n)
        bass_part.append(music21.note.Rest(duration=n.duration))
    score.insert(0, treble_part)
    score.insert(0, bass_part)
    score.show()
notes1 = ["G2", "C4", "C#5", "D4", "F#4", "D#5", "E4", "F4", "F#5", "G4", "G#4", "A4", "A#4", "B4"]
list2score(notes1, "eighth")
notes2 = ["B4", "D4", "F#4", "D#4", "E2", "F3", "B#5", "G3", "G#4", "A4", "D#3", "C4"]
list2score(notes2, "quarter")
