import random

CRASH_PROBABILITY = 0.045  # 4.5% chance


def simulate_crashes(days: int) -> float:
    crashes = 0
    for _ in range(days):
        if random.random() < CRASH_PROBABILITY:
            crashes += 1
    return crashes / days