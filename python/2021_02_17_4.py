# python
# Converts an angle from radian to degrees.

import math

def radianToDegrees(radian):
    return (radian * 180.0) / math.pi

radian = math.pi/4
print(radianToDegrees(radian))
