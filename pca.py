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
T = np.array(matrix)
pca = PCA(n_components=3)
pca.fit(T)
print(pca.explained_variance_ratio_)
