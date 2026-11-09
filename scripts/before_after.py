"""Create docs/previews/*: a 'before' (matplotlib defaults) vs 'after' (publication style) comparison."""
import importlib.util
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "previews"; OUT.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(ROOT / "data" / "sensor_experiment.csv", parse_dates=["timestamp"]).dropna()

mpl.rcdefaults()
fig, ax = plt.subplots(figsize=(3.4, 2.4))
ax.scatter(df.temperature_c, df.power_w, s=10)            # defaults: overplotted, no site info, tiny fonts at print size
ax.set_xlabel("temperature_c"); ax.set_ylabel("power_w")
fig.savefig(OUT / "figure_before.svg", bbox_inches="tight")
plt.close(fig)

spec = importlib.util.spec_from_file_location("gf", ROOT / "scripts" / "generate_figures.py")
gf = importlib.util.module_from_spec(spec); spec.loader.exec_module(gf)
gf.setup_style(); mpl.rcParams["svg.fonttype"] = "path"
d = gf.load()
fig, ax = plt.subplots(figsize=(3.4, 2.4), constrained_layout=True)
gf.panel_scatter(ax, d)
fig.savefig(OUT / "figure_after.svg", bbox_inches="tight")
print("wrote previews")
