import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 数据点
data = np.array([[1, 2], [2, 1], [3, 4], [5, 7], [8, 9], [10, 10]])

# K-means聚类
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 可视化
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')
plt.title('K-means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
