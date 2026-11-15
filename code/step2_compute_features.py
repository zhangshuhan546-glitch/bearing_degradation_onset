import pandas as pd
import numpy as np
from scipy.stats import kurtosis #现成的峭度函数

DATA_ROOT = "../data/35Hz12kN"
x = pd.read_csv(f"{DATA_ROOT}/Bearing1_1/1.csv")["Horizontal_vibration_signals"].values

rms = np.sqrt(np.mean(x**2))
p2p = x.max() - x.min()
kurt = kurtosis(x,fisher=False) #把x交给这个函数解决
"""
峭度约等于3：信号平稳，没有突出尖峰。
峭度明显大于3：信号中有突出尖峰。
"""
print("RMS\n",rms)
print("峰峰值\n",p2p)
print("峭度\n",kurt)

