"""Compare an unstyled scatter plot with the publication-style figure.

Run python scripts/make_data.py first. SVG outputs are written to
dist/previews/before-after/ and are local build products, not committed
portfolio previews.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from generate_figures import load, panel_scatter, setup_style

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sensor_experiment.csv"
OUTPUT = ROOT / "dist" / "previews" / "before-after"


def main() -> None:
    """Create the before-and-after SVG comparison."""
    OUTPUT.mkdir(parents=True, exist_ok=True)
    raw = pd.read_csv(DATA, parse_dates=["timestamp"]).dropna()

    mpl.rcdefaults()
    figure, axis = plt.subplots(figsize=(3.4, 2.4))
    axis.scatter(raw["temperature_c"], raw["power_w"], s=10)
    axis.set_xlabel("temperature_c")
    axis.set_ylabel("power_w")
    figure.savefig(OUTPUT / "figure_before.svg", bbox_inches="tight")
    plt.close(figure)

    setup_style()
    data = load()
    figure, axis = plt.subplots(figsize=(3.4, 2.4), constrained_layout=True)
    panel_scatter(axis, data)
    figure.savefig(OUTPUT / "figure_after.svg", bbox_inches="tight")
    plt.close(figure)
    print(f"Wrote before-and-after previews to {OUTPUT}")


if __name__ == "__main__":
    main()
