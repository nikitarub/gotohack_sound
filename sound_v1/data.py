import wave
import numpy as np
import os


# Типы данных амплитуд
types = {
    1: np.int8,
    2: np.int16,
    4: np.int32,
}


# Открытие файла на рвзбор
# Переделать !!!!

#filepath = '/Users/nikita/Desktop/misc/DP_Flute02_86_Amin.wav'

# Сделай общий вид

def wave_open(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        wavf =  wave.open(filepath, mode='r')
        return wavf

wav = wave_open('/Users/nikita/Desktop/misc/Eee_2.wav')
# Различные вкусности из wave-файла
def nchannals():
    nchannals_var = wav.getnchannels()
    return nchannals_var

def sampwidth():
    sampwidth_var = wav.getsampwidth()
    return  sampwidth_var

def framerate():
    framerate_var = wav.getframerate()
    return framerate_var

def nframes():
    nframes_var = wav.getnframes()
    return  nframes_var

def comptype():
    comptype_var = wav.getcomptype()
    return comptype_var

def compname():
    compname_var = wav.getcompname()
    return compname_var


def duration():
    duration_var = nframes()/framerate()
    return duration_var

# Значения амплитуд в 10-ричной системе счисления
def channel_data():
    byte_content = wav.readframes(nframes())
    samples = np.fromstring(byte_content, dtype=types[sampwidth()])
    #for n in range(nchannals()):
    channel = samples
    return channel

