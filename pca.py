from sklearn.decomposition import PCA
import numpy as np
import json

lineFile = open('countLine.json', encoding='utf-8')
res = lineFile.read()
lines = json.loads(res)

markFile = open('markLevel.json', encoding='utf-8')
res = markFile.read()
marks = json.loads(res)

pyFile = open('pyPercent.json', encoding='utf-8')
res = pyFile.read()
pyPercent = json.loads(res)

matrix = []
for k in lines.keys():
    matrix.append([lines[k], marks[k], pyPercent[k]])

# 标准化
average = []
distance = []
for i in range(3):
    minI = 0
    maxI = 1000
    total = 0
    for k in range(len(matrix)):
        minI = min(minI, matrix[k][i])
        maxI = max(maxI, matrix[k][i])
        total += matrix[k][i]
    distance.append(maxI-minI)
    average.append(total/len(matrix))

for i in range(3):
    for k in range(len(matrix)):
        matrix[k][i] = (matrix[k][i] - average[i])/distance[i]
print(matrix)

T = np.array(matrix)
pca = PCA(n_components=3, whiten=True)
pca.fit(T)
print("行数 分数 py占比")
print(pca.explained_variance_ratio_)

