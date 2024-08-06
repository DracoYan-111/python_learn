import numpy as np
from scipy.integrate import solve_ivp
import pysindy as ps
import matplotlib.pyplot as plt

# Lorenz 系统方程
def lorenz(t, state):
    x, y, z = state
    sigma = 10
    rho = 28
    beta = 8 / 3
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

# 时间范围
dt = 0.01
t = np.arange(0, 25, dt)

# 初始条件
x0 = [1, 1, 1]

# 生成数据
sol = solve_ivp(lorenz, [t[0], t[-1]], x0, t_eval=t)
data = sol.y.T

# 创建并拟合 SINDy 模型
model = ps.SINDy()
model.fit(data, t=dt)
model.print()

# 预测数据
x_pred = model.simulate(data[0], t)

# 可视化实际数据与预测数据
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 8))
for i, ax in enumerate(axs):
    ax.plot(t, data[:, i], 'k', label='True')
    ax.plot(t, x_pred[:, i], 'r--', label='Identified')
    ax.set_ylabel(['x', 'y', 'z'][i])
axs[-1].set_xlabel('Time')
axs[0].legend()
plt.show()
