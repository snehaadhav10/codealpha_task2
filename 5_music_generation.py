
import numpy as np
import random

start = np.random.randint(0, len(network_input) - 1)
pattern = network_input[start]
int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

prediction_output = []

for note_index in range(500):
    prediction_input = np.reshape(pattern, (1, len(pattern), 1))
    prediction_input = prediction_input / float(len(pitchnames))
    prediction = model.predict(prediction_input, verbose=0)
    index = np.argmax(prediction)
    result = int_to_note[index]
    prediction_output.append(result)
    pattern = np.append(pattern, index)
    pattern = pattern[1:len(pattern)]
