import math
from typing import List, Union

Number = Union[int, float]


class StatEngine:
    def __init__(self, data: List[Number]):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Data must be a list or tuple.")

        # Clean numeric values only
        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(x)
            elif x is None:
                continue
            else:
                raise TypeError(f"Invalid data type detected: {type(x)}")

        if len(cleaned) == 0:
            raise ValueError("Data array is empty after cleaning.")

        self.data = cleaned

    # ------------------------------
    # CENTRAL TENDENCY
    # ------------------------------

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def get_mode(self):
        counts = {}
        for value in self.data:
            counts[value] = counts.get(value, 0) + 1

        max_count = max(counts.values())

        if max_count == 1:
            return "No mode — all values appear only once."

        modes = [k for k, v in counts.items() if v == max_count]
        return modes

    # ------------------------------
    # DISPERSION
    # ------------------------------

    def get_variance(self, is_sample=True):
        n = len(self.data)

        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")

        mean = self.get_mean()
        total = sum((x - mean) ** 2 for x in self.data)

        if is_sample:
            return total / (n - 1)   # Bessel correction
        else:
            return total / n         # Population variance

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # ------------------------------
    # OUTLIER DETECTION
    # ------------------------------

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        sd = self.get_standard_deviation()

        return [
            x for x in self.data
            if abs(x - mean) > threshold * sd
        ]