
import numpy as np

sequence_length = 100
pitchnames = sorted(set(item for item in notes))
note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

network_input = []
network_output = []

for i in range(0, len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length]
    network_input.append([note_to_int[char] for char in seq_in])
    network_output.append(note_to_int[seq_out])

network_input = np.reshape(network_input, (len(network_input), sequence_length, 1))
network_input = network_input / float(len(pitchnames))
