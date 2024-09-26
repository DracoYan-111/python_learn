import pandas as pd
import numpy as np

# 创建数据集
data = {
    'Date': pd.date_range(start='2022-05-10', periods=7, freq='D'),
    'VAS_Score': np.random.randint(0, 10, size=7)
}

# 创建 DataFrame
df = pd.DataFrame(data)
# 计算疼痛评分的平均值、标准差等指标

df['VAS_Score'].describe()

import matplotlib.pyplot as plt

# 绘制折线图
plt.plot(df['Date'], df['VAS_Score'], marker='o')
plt.title('VAS Score Trend Over Time')
plt.xlabel('Date')
plt.ylabel('VAS Score')
plt.grid(True)
plt.show()
