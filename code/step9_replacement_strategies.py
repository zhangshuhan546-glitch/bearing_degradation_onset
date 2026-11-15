#三个不同策略的更换成本
#寿命和退化起点均来自step8的输出
lives = [123,161,158,122,52]  #五个轴承的寿命
starts=[70,37,59,88,30]
fail_cost=100     #失效一次的成本（假设）

 # 坏了再换
total=0
for life in lives:
    cost=fail_cost
    total=cost+total
print("总成本", total,"平均",total/len(lives))

# 定期更换
T = 120                              # 定期更换的时间
total = 0
for life in lives:
    if life<=120:                      # 填：什么条件下轴承已经先坏了
        cost = fail_cost
    else:
        cost = life-120               # 填：提前换，浪费了多少寿命
    total = total + cost
print("T =", T, "总成本", total, "平均", total / len(lives))
# 最优T
for T in range(10, 171, 10):          # T 从 10 到 170，每次加 10
    total = 0
    for life in lives:
        if life <= T:
            cost = fail_cost
        else:
            cost = life - T
        total = total + cost
    print("T =", T, "平均", total / len(lives))

# 检测到退化后，运行D分钟后换
for D in range(0, 61, 5):
    total = 0
    for life, s in zip(lives, starts):
        replace_time = s + D
        if replace_time>=life :                  # 填：还没换就已经坏了的条件
            cost = fail_cost
        else:
            cost = life-replace_time          # 填：提前换，浪费了多少寿命
        total = total + cost
    print("D =", D, "平均", total / len(lives))


