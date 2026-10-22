# Bode-Plots for the data gathered at the measuring lab

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filter_data = pd.read_excel("Preamp_Filter_Data.xlsx", sheet_name="Filter")
preamp_data = pd.read_excel("Preamp_Filter_Data.xlsx", sheet_name="Preamp")

for df in (filter_data, preamp_data):
    df.columns = ["f", "gain_dB", "fase"]


filter_data = filter_data.apply(pd.to_numeric, errors="coerce")
preamp_data = preamp_data.apply(pd.to_numeric, errors="coerce")

filter_data.loc[filter_data["fase"] == 0, "fase"] = np.nan

answer = input("filter eller amp?: ").strip()

if answer == "filter":
    obj = filter_data
elif answer == "amp":
    obj = preamp_data
else:
    raise ValueError("Bro skriv inn ett av alternativene")

fig, ax1 = plt.subplots()
ax1.semilogx(obj["f"], obj["gain_dB"], color="r", label="Gain")
ax1.set_xlabel("Frequency [Hz]")
ax1.set_ylabel("Gain [dB]", color="r")
ax1.grid(True, which="both")

ax2 = ax1.twinx()
ax2.semilogx(obj["f"], obj["fase"], color="b", label="Phase")
ax2.set_ylabel("Phase [deg]", color="b")

lines = ax1.get_lines() + ax2.get_lines()
ax2.legend(handles=lines, loc="best")

ax1.set_title(f"{answer} bode-plot", size=15)
fig.tight_layout()
plt.show()