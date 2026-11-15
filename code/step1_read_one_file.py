import pandas as pd 
import matplotlib.pyplot as plt

DATA_ROOT = "../data/35Hz12kN"
df = pd.read_csv(f"{DATA_ROOT}/Bearing1_1/1.csv")

print(df.shape) #行数加列数
print(df.head())

x = df["Horizontal_vibration_signals"].values
plt.figure(figsize=(10,3))
plt.plot(x[:500])
plt.title("Bearing1_1 minutes Horizontal")
plt.show()

