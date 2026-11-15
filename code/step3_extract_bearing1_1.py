import os
import numpy as np
import pandas as pd
from scipy.stats import kurtosis

DATA_ROOT = "../data/35Hz12kN"
folder = f"{DATA_ROOT}/Bearing1_1"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]  #os.listdir(folder)列出 folder 里面的所有文件
files.sort(key=lambda x: int(x.replace(".csv","")))
print("文件数\n", len(files))

rows = []
for f in files:
    x = pd.read_csv(os.path.join(folder, f))["Horizontal_vibration_signals"].values
    rows.append({
        "minute":int(f.replace(".csv","")),
        "rms":np.sqrt(np.mean(x**2)),
        "p2p":x.max()-x.min(),
        "kurtosis":kurtosis(x,fisher=False),
    })
feat = pd.DataFrame(rows)
feat.to_csv("Bearing1_1_features.csv", index=False)
print(feat.shape)


