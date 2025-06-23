
from music21 import stream, note, chord

offset = 0
output_notes = []

for pattern in prediction_output:
    if ('.' in pattern) or pattern.isdigit():
        notes_in_chord = pattern.split('.')
        chord_notes = [note.Note(int(n)) for n in notes_in_chord]
        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)
    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        output_notes.append(new_note)
    offset += 0.5

midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='generated_music.mid')
