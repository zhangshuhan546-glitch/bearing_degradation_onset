import pandas as pd
import matplotlib.pyplot as plt

names = ["Bearing1_1", "Bearing1_2", "Bearing1_3", "Bearing1_4", "Bearing1_5"]

fig, axes = plt.subplots(5, 1, figsize=(10, 12)) #分别返回整个画布和
for ax, name in zip(axes, names):
    feat = pd.read_csv(f"../features/{name}_features.csv")
    ax.plot(feat["minute"], feat["rms"])
    ax.set_ylabel(name)
    print(name, "寿命:", len(feat), "分钟")
axes[-1].set_xlabel("minute") #axes[-1]清单的最下面的一个格子
plt.tight_layout()
plt.savefig("../figures/bearing_1_to_5_RMS_compare.png",dpi=300)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt


