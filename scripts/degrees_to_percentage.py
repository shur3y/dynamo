# convert degrees to percentage slope and vice versa

import math


def convert(input_number):
    try:
        percentage = "{:.2f}%".format(math.tan(math.radians(float(input_number))) * 100)
        degrees = "{:.2f}°".format(math.degrees(math.atan(float(input_number) / 100)))
        return "Percentage: %s, degrees: %s" % (percentage, degrees)
    except ValueError:
        return None


OUT = convert(IN[0])
