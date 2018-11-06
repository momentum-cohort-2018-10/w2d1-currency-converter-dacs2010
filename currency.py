def convert(rate , value, current, to):
    if current is to:
        return value
    for i in rate:
        if i[0] is current and i[1] is to:
            return value * i[2]
        if i[1] is current and i[0] is to:
            return value / i[2]
    raise ValueError(f"Something is wrong with {current} {to}")
    raise ValueError(f"Could it be {rate} {value}")
