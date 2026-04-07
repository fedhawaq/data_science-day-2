from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

def main():
    print("\n=== Statistical Engine Demo ===")

    data = [2300, 4000, 7000, 7500, 8000, 9500, 1000000]

    engine = StatEngine(data)

    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Sample Variance:", engine.get_variance())
    print("Sample SD:", engine.get_standard_deviation())
    print("Outliers:", engine.get_outliers())

    print("\n=== Monte Carlo Simulation ===")
    for days in [30, 365, 10000]:
        simulated_p = simulate_crashes(days)
        print(f"Days={days}, Simulated Crash Probability={simulated_p:.4f}")

if __name__ == "__main__":
    main()