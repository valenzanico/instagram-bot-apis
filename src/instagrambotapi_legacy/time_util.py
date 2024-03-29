"""from https://github.com/timgrossmann/InstaPy"""
"""Helper module to handle time related stuff"""
from time import sleep as original_sleep
from datetime import datetime
from random import gauss
from numpy.random import default_rng
uniform = default_rng().uniform
# Amount of variance to be introduced
# i.e. random time will be in the range: TIME +/- STDEV %
STDEV = 0.5
sleep_percentage = 1
sleep_percentage = sleep_percentage * uniform(0.9, 1.1)


def randomize_time(mean):
    allowed_range = mean * STDEV
    stdev = allowed_range / 3  # 99.73% chance to be in the allowed range

    t = 0
    while abs(mean - t) > allowed_range:
        t = gauss(mean, stdev)

    return t


def set_sleep_percentage(percentage):
    global sleep_percentage
    sleep_percentage = percentage / 100
    sleep_percentage = sleep_percentage * uniform(0.9, 1.1)


def sleep(t, custom_percentage=None):
    if custom_percentage is None:
        custom_percentage = sleep_percentage
    time = randomize_time(t) * custom_percentage
    original_sleep(time)


def sleep_actual(t):
    original_sleep(t)


def get_time(labels):
    """To get a use out of this helpful function
    catch in the same order of passed parameters"""
    if not isinstance(labels, list):
        labels = [labels]

    results = []

    for label in labels:
        if label == "this_minute":
            results.append(datetime.now().strftime("%M"))

        if label == "this_hour":
            results.append(datetime.now().strftime("%H"))

        elif label == "today":
            results.append(datetime.now().strftime("%Y-%m-%d"))

    results = results if len(results) > 1 else results[0]

    return results


def random_sleep(inf=0.5, sup=3.0, modulable=True, log=True):
    speed_multiplier = 1.0
    MIN_INF = 0.3
    multiplier = float(speed_multiplier)
    delay = uniform(inf, sup) / (multiplier if modulable else 1.0)
    delay = max(delay, MIN_INF)
    sleep(delay)