import math


def pulse(
    time,
    speed=0.05,
    amount=1
):

    return math.sin(
        time * speed
    ) * amount
