import data as dt

# Получение из data значений амплетуд волны
def get_peaks():
    peaks = dt.channel_data()
    return peaks

# Сжатие значений в pinch_value раз, формирование массива
def get_pinching():
    peaks_sum = 0
    pinched_peaks = []
    pinch_value = 8
    #peaks = get_peaks()
    for index,peak in enumerate(get_peaks()):
        peaks_sum += peak
        if (index+1) % pinch_value == 0:
            pinched_peaks.append(int(peaks_sum/pinch_value))
            peaks_sum = 0
    return pinched_peaks

# Кол-во значений после сжатия
def get_pinching_lenght():
    length = len(get_pinching())
    return length


