"""Publication-quality figure pipeline.

Reads data/sensor_experiment.csv, cleans it, computes summary statistics and
exports (i) four individual panels for a LaTeX subfigure environment,
(ii) a combined 2x2 figure, (iii) a siunitx-ready LaTeX table.

Outputs are vector PDF/SVG (plus a 300 dpi PNG preview of the combined figure).
Run:  python scripts/generate_figures.py
"""
import os
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sensor_experiment.csv"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

# Okabe-Ito colour-blind-safe palette
OI = {"black": "#000000", "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73",
      "yellow": "#F0E442", "blue": "#0072B2", "verm": "#D55E00", "purple": "#CC79A7"}
SITE_COLORS = {"Site A": OI["blue"], "Site B": OI["orange"], "Site C": OI["green"]}

# Font sizes chosen to match 10 pt body text / 8 pt captions of a journal paper
def setup_style():
    # Default: matplotlib's bundled Computer Modern (cmr10) + mathtext 'cm' -> matches LaTeX body font
    # without requiring a TeX install. Set USE_TEX=1 to render all text with real LaTeX
    # (needs latex, dvipng-free PDF backend and the cm-super package).
    use_tex = os.environ.get("USE_TEX") == "1"
    mpl.rcParams.update({
        "text.usetex": use_tex,
        "font.family": "serif",
        "font.serif": ["Computer Modern Roman"] if use_tex else ["cmr10"],
        "mathtext.fontset": "cm",
        "axes.formatter.use_mathtext": True,
        "axes.unicode_minus": False,
        "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
        "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7,
        "axes.linewidth": 0.6, "lines.linewidth": 1.0,
        "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "figure.dpi": 100, "savefig.dpi": 300, "pdf.fonttype": 42, "svg.fonttype": "none" if not use_tex else "path",
        "axes.prop_cycle": mpl.cycler(color=[OI["blue"], OI["orange"], OI["green"], OI["verm"], OI["purple"]]),
    })
    sns.set_theme(style="ticks", rc=dict(mpl.rcParams))
    mpl.rcParams.update({"text.usetex": use_tex})


def load():
    df = pd.read_csv(DATA, parse_dates=["timestamp"])
    n_missing = int(df[["temperature_c", "power_w"]].isna().sum().sum())
    df = df.sort_values("timestamp").set_index("timestamp")
    num = ["temperature_c", "humidity_pct", "power_w", "vibration_g"]
    df[num] = df[num].interpolate(limit_direction="both")  # time-ordered gap fill
    print(f"loaded {len(df)} rows, interpolated {n_missing} missing values")
    return df


LABELS = {"temperature_c": r"Temperature", "humidity_pct": r"Humidity",
          "power_w": r"Power", "vibration_g": r"Vibration"}


def panel_timeseries(ax, df):
    daily = df["power_w"].resample("D").agg(["mean", "std"])
    ax.fill_between(daily.index, daily["mean"] - daily["std"], daily["mean"] + daily["std"],
                    color=OI["sky"], alpha=0.35, lw=0, label=r"$\pm 1$ s.d.")
    ax.plot(daily.index, daily["mean"], color=OI["blue"], label="Daily mean")
    ax.set_ylabel("Power (W)"); ax.set_xlabel("Date (2025)")
    ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%b"))
    ax.legend(frameon=False, loc="upper left")


def panel_heatmap(ax, df):
    corr = df[list(LABELS)].corr()
    names = [LABELS[c] for c in corr.columns]
    sns.heatmap(corr, ax=ax, annot=True, fmt=".2f", vmin=-1, vmax=1, cmap="vlag",
                xticklabels=names, yticklabels=names, linewidths=0.5, square=True,
                annot_kws={"size": 6.5}, cbar_kws={"shrink": 0.8, "label": r"Pearson $r$"})
    ax.tick_params(axis="x", rotation=30); ax.tick_params(axis="y", rotation=0)


def panel_boxplot(ax, df):
    d = df.reset_index()
    sns.boxplot(data=d, x="site", y="power_w", hue="site", palette=SITE_COLORS, ax=ax,
                linewidth=0.7, fliersize=1.5, legend=False, width=0.6)
    ax.set_xlabel(""); ax.set_ylabel("Power (W)")


def panel_scatter(ax, df):
    s = df.sample(600, random_state=1).reset_index()
    sns.scatterplot(data=s, x="temperature_c", y="power_w", hue="site", palette=SITE_COLORS,
                    s=6, linewidth=0, alpha=0.7, ax=ax)
    m, b = np.polyfit(df["temperature_c"], df["power_w"], 1)
    xs = np.linspace(df["temperature_c"].min(), df["temperature_c"].max(), 50)
    ax.plot(xs, m * xs + b, color=OI["black"], lw=0.8, ls="--")
    ax.set_xlabel(r"Temperature ($^\circ$C)"); ax.set_ylabel("Power (W)")
    ax.legend(frameon=False, title=None, loc="upper left", markerscale=1.5)


PANELS = {"a": panel_timeseries, "b": panel_heatmap, "c": panel_boxplot, "d": panel_scatter}


def save(fig, stem):
    for ext in ("pdf", "svg"):
        fig.savefig(FIG / f"{stem}.{ext}", bbox_inches="tight")


def export_tables(df):
    g = (df.reset_index().groupby("site")
         .agg(n=("power_w", "size"), temp=("temperature_c", "mean"),
              power_m=("power_w", "mean"), power_s=("power_w", "std"),
              vib=("vibration_g", "mean")))
    lines = [r"% AUTO-GENERATED by scripts/generate_figures.py -- do not edit",
             r"\begin{tabular}{@{}l S[table-format=4.0] S[table-format=2.2] S[table-format=3.2] S[table-format=2.2] S[table-format=1.3]@{}}",
             r"\toprule",
             r"{Site} & {$n$} & {$\bar T$ (\si{\celsius})} & {$\bar P$ (\si{\watt})} & {$s_P$ (\si{\watt})} & {$\bar a$ (\si{\gforce})} \\",
             r"\midrule"]
    for site, r in g.iterrows():
        lines.append(f"{site} & {int(r.n)} & {r.temp:.2f} & {r.power_m:.2f} & {r.power_s:.2f} & {r.vib:.3f} \\\\")
    lines += [r"\bottomrule", r"\end{tabular}"]
    (FIG / "summary_table.tex").write_text("\n".join(lines) + "\n")
    g.round(4).to_csv(FIG / "summary_stats.csv")
    r_tp = df["temperature_c"].corr(df["power_w"])
    (FIG / "key_numbers.tex").write_text(
        f"\\newcommand{{\\rTP}}{{{r_tp:.2f}}}\n\\newcommand{{\\Nobs}}{{{len(df)}}}\n")
    print(g.round(3)); print(f"corr(temperature, power) = {r_tp:.3f}")


def main():
    setup_style()
    df = load()
    for key, fn in PANELS.items():  # individual panels (for LaTeX subfigure)
        fig, ax = plt.subplots(figsize=(3.4, 2.4), constrained_layout=True)
        fn(ax, df); save(fig, f"fig_panel_{key}"); plt.close(fig)
    fig, axes = plt.subplots(2, 2, figsize=(7.16, 5.2), constrained_layout=True)
    for (key, fn), ax in zip(PANELS.items(), axes.ravel()):
        fn(ax, df); ax.set_title(f"({key})", loc="left")
    save(fig, "fig_multipanel")
    fig.savefig(FIG / "fig_multipanel.png", dpi=300)
    plt.close(fig)
    export_tables(df)


if __name__ == "__main__":
    main()
