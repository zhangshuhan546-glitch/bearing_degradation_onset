import pandas as pd
import matplotlib.pyplot as plt

feat = pd.read_csv("../features/Bearing1_1_features.csv")

fig, axes = plt.subplots(3,1,figsize=(10,8),sharex=True)
for ax,col in zip(axes,["rms","kurtosis","p2p"]):
    ax.plot(feat["minute"],feat[col])
    ax.set_ylabel(col)
axes[-1].set_xlabel("minute")
plt.tight_layout()
plt.savefig("../figures/Bearing1_1_features.png")
plt.show()
