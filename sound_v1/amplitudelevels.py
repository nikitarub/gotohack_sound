import pinch as p


# Получение урезанных значений из амплитуд
def get_pinched_peaks():
    pinched_peaks = p.get_pinching()
    return pinched_peaks


# Сколько раз 256 полностью содержится в значении амплетуды
def get_relate(amplitude_value):
    relate = -1
    minus = False
    if amplitude_value < 0:
        minus = True
        while amplitude_value < 0:
            amplitude_value = amplitude_value + 256
            relate +=1
    elif amplitude_value >= 0:
        while amplitude_value > 0:
            amplitude_value = amplitude_value - 256
            relate +=1
    if relate == -1:
        relate = 0
    return relate,minus

# Уровень амплитуды
def get_level(relate,minus):
    if minus:
        level = -relate
    else: level = relate
    return level

# Формирование массива из уровней
def get_all_levels():
    pinched_peaks = get_pinched_peaks()
    pinched_amplitudes = []
    for peak in pinched_peaks:
        relate,minus = get_relate(peak)
        level = get_level(relate,minus)
        pinched_amplitudes.append(level)
    return pinched_amplitudes

