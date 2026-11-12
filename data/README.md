# Generated dataset

The CSV in this folder is created by [../scripts/make_data.py](../scripts/make_data.py). From the repository root, run:

    python scripts/make_data.py

The script creates 2,880 hourly rows covering 1 January to 30 April 2025. Each row is assigned to Site A, Site B or Site C. Columns record the timestamp, site, temperature, humidity, power and vibration.

The generator inserts 25 missing temperature values and 25 missing power values. [generate_figures.py](../scripts/generate_figures.py) fills those gaps before creating the charts and summary table.

All values are simulated with a fixed random seed. They are not measurements from real buildings, equipment or monitoring sites. Git ignores the CSV because the generator can recreate it; change the script rather than editing the output by hand.
