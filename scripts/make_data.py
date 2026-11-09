"""Generate the SYNTHETIC demo dataset used by the portfolio.

All values are simulated (fixed random seed) -- no real measurements.
Run:  python scripts/make_data.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
OUT = Path(__file__).resolve().parents[1] / "data" / "sensor_experiment.csv"

n_days = 120
t = pd.date_range("2025-01-01", periods=n_days * 24, freq="h")
hours = np.arange(len(t))

temp = 20 + 6 * np.sin(2 * np.pi * hours / 24 - 1.5) + 3 * np.sin(2 * np.pi * hours / (24 * 30)) + rng.normal(0, 0.8, len(t))
humidity = 55 - 1.4 * (temp - 20) + rng.normal(0, 3, len(t))
power = 120 + 4.5 * np.clip(temp - 18, 0, None) + rng.normal(0, 6, len(t))
vibration = 0.2 + 0.02 * np.abs(temp - 20) + rng.gamma(2.0, 0.05, len(t))

sites = rng.choice(["Site A", "Site B", "Site C"], size=len(t), p=[0.4, 0.35, 0.25])
offset = pd.Series(sites).map({"Site A": 0.0, "Site B": 4.0, "Site C": -3.0}).to_numpy()
power = power + offset

df = pd.DataFrame({
    "timestamp": t, "site": sites,
    "temperature_c": temp.round(3), "humidity_pct": humidity.round(3),
    "power_w": power.round(3), "vibration_g": vibration.round(4),
})
# a few gaps for the cleaning step to handle
for col in ["temperature_c", "power_w"]:
    idx = rng.choice(len(df), size=25, replace=False)
    df.loc[idx, col] = np.nan
df.to_csv(OUT, index=False)
print(f"wrote {OUT} ({len(df)} rows)")
