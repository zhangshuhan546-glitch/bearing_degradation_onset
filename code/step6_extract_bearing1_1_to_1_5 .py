import os
import numpy as np
import pandas as pd
from scipy.stats import kurtosis

ATA_ROOT = "../data/35Hz12kN"
root = DATA_ROOT
bearings = ["Bearing1_2", "Bearing1_3", "Bearing1_4", "Bearing1_5"]

for name in bearings:
    folder = os.path.join(root, name)
    files = [f for f in os.listdir(folder) if f.endswith(".csv")]
    files.sort(key=lambda f: int(f.replace(".csv", "")))

    rows = []
    for f in files:
        x = pd.read_csv(os.path.join(folder, f))["Horizontal_vibration_signals"].values
        rows.append({
            "minute": int(f.replace(".csv", "")),
            "rms": np.sqrt(np.mean(x ** 2)),
            "p2p": x.max() - x.min(),
            "kurtosis": kurtosis(x, fisher=False),
        })

    feat = pd.DataFrame(rows)
    feat.to_csv(f"../features/{name}_features.csv", index=False)
    print(name, "完成，共", len(feat), "分钟")
