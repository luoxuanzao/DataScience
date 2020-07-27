from sklearn.cluster import KMeans
import numpy as np
import json
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans  # Kmeans
from sklearn.preprocessing import MinMaxScaler  # 数据标准化包
# x效果评估模块
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
import matplotlib  as mp1

f1 = open("countLine.json")
f2 = open("pyPercent.json")
f3 = open("markLevel.json")
lines = json.load(f1)
py = json.load(f2)
mark = json.load(f3)
arrays = []
plt.rcParams['font.sans-serif'] = ['SimHei']

# arrayLines = []
# arrayPy = []
# arrayMark = []
lineArray = []
pyArray = []
markArray = []
arrayRank = []
resultArray = []


def standardizing(array, positive):
    Max = max(array)
    Min = min(array)
    if positive:
        for i in range(len(array)):
            array[i] = (array[i] - Min) / (Max - Min) * 100
    else:
        for i in range(len(array)):
            array[i] = (Max - array[i]) / (Max - Min) * 100
    return array


def getArray(lineArray, pyArray, markArray):
    for key in py:
        lineArray.append(lines[key])
        pyArray.append(py[key])
        markArray.append(mark[key])
    lineArray = standardizing(lineArray, True)
    pyArray = standardizing(pyArray, False)
    markArray = standardizing(markArray, False)
    for i in range(len(pyArray)):
        arrayRank.append(lineArray[i] * 0.183880 + pyArray[i] * 0.443304 + markArray[i] * 0.372815)
    resultArray = np.array(arrayRank).reshape(-1, 1)
    return np.array(arrayRank).reshape(-1, 1)


def calKmeans(X):
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    center = kmeans.cluster_centers_
    result = kmeans.labels_
    # 非监督式评估方法
    # 平均轮廓系数
    silhouette_s = silhouette_score(X, kmeans.labels_, metric='euclidean')
    # calinski和harabaz得分
    calinski_harabaz_s = calinski_harabasz_score(X, kmeans.labels_)
    print('silhouette_s: %f \n calinski_harabaz_s: %f' % (silhouette_s, calinski_harabaz_s))

    # print(result)
    temp = sorted(center)
    print(temp)
    # print(center)
    # print(temp)
    index = []
    for i in range(len(temp)):
        print(temp.index(center[i]))
        index.append(temp.index(center[i]))
    # print(index)
    re = {}
    i = 0
    for key in py:
        re[key] = int(result[i])
        i += 1
    # print(re)
    # print(type(re))
    difficulty = [0, 0, 0, 0, 0]
    detail = ["最简单", "较简单", "中等", "较难", "最难"]
    for key in re:
        print(key, end=" ")
        difficulty[index[re[key]]] += 1
        print(detail[index[re[key]]])
    for i in range(len(difficulty)):
        print(detail[i], ":" + str(difficulty[i]))
    # plt.axes(aspect='equal')
    # plt.pie(difficulty, labels=detail, autopct='%.0f%%')
    plt.title("各分数段频数")


calKmeans(getArray(lineArray, pyArray, markArray))
print(arrayRank)

plt.hist(
    x=arrayRank,
    bins=100,
    color='steelblue',  # 指定直方图的填充色
    edgecolor='blue'  # 指定直方图的边框色
)
plt.savefig("number.jpg")
plt.show()
