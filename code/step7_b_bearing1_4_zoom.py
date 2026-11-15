import pandas as pd
import matplotlib.pyplot as plt

feat = pd.read_csv("../features/Bearing1_4_features.csv")
feat =feat.iloc[:-3] #去掉后三分钟的数据
fig, axes = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
axes[0].plot(feat["minute"], feat["rms"])
axes[0].set_ylabel("rms")
axes[1].plot(feat["minute"], feat["kurtosis"])
axes[1].set_ylabel("kurtosis")
axes[1].set_xlabel("minute")
plt.tight_layout()
plt.savefig("../figures/bearing_4_zoom.png",dpi=300)
plt.show()