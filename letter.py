def char_frequency(pavana):
    dict = {}
    for n in pavana:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('ishana'))
