import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

feat  = pd.read_csv("../features/Bearing1_1_features.csv")
rms = feat["rms"].values

# 前20分钟当健康基线，算警戒线
base = rms[:20]
thr = base.mean()+3*base.std()

# 找第一次连续3个点都超过警戒线的位置
above = rms>thr
fpt =None
for i in range(20,len(rms)-2):
    if above[i] and above[i+1] and above[i+2]:
        fpt = i
        break
print("警戒线:", thr)
print("退化起点位置:", fpt, " 对应分钟:", feat["minute"].iloc[fpt])

# 画图：曲线 + 警戒线 + 起点
plt.figure(figsize=(10, 3))
plt.plot(feat["minute"], rms)
plt.axhline(thr, color="orange", linestyle="--")
plt.axvline(feat["minute"].iloc[fpt], color="red")
plt.savefig("../figures/bearing_1_1_degradation.png",dpi=300)
plt.show()
for n_base in [20, 30, 40, 50]:
    for consec in [3, 5]:
        base = rms[:n_base]
        thr = base.mean() + 3 * base.std()
        above = rms > thr
        result = None
        for i in range(n_base, len(rms) - consec + 1):
            if above[i:i + consec].all():
                result = i
                break
        print("基线", n_base, "连续", consec, "→ 起点", result)
