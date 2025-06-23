
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation
from keras.utils import np_utils

model = Sequential()
model.add(LSTM(512, input_shape=(network_input.shape[1], network_input.shape[2]), return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(512))
model.add(Dense(256))
model.add(Dropout(0.3))
model.add(Dense(len(pitchnames)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

network_output = np_utils.to_categorical(network_output)
model.fit(network_input, network_output, epochs=100, batch_size=64)
