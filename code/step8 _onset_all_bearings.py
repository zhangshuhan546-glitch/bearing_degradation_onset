import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ["Bearing1_1", "Bearing1_2", "Bearing1_3", "Bearing1_4", "Bearing1_5"]                              # 5个名字（你已写对）

for name in names:
    feat = pd.read_csv(f"../features/{name}_features.csv")             # 填：读 f"{name}_features.csv"
    rms = feat["rms"].values
    # 开头的注释 starts = []

    base = rms[:20]
    thr = base.mean()+3*base.std()                           # 填：均值 + 3倍标准差

    above = rms > thr
    fpt = None #First Predicting Time
    for i in range(20, len(rms) - 2):
        if above[i] and above[i+1] and above[i+2]:                         # 填：三个连续超线,都为True
            fpt = i   #给fpt一个终断的值
            break
#每次都会把fpt清空
    if fpt is not None:
        print(name, "寿命", len(rms), "起点", feat["minute"].iloc[fpt])  #iloc是按位置取值
        print("退化起点的占比分别为",feat["minute"].iloc[fpt]/len(rms))
    else:
        print(name, "寿命", len(rms), "未检测到起点")



