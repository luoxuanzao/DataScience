# 极差法数据标准化
import json


def std(myList):
    resPath = myList[0]
    outPath = myList[1]
    # 该指标是否为正向指标，即指标数值越大对结果是越好还是越坏，越好则为正向指标，isPositive为True，否则False
    isPositive = myList[2]
    f = open(resPath, encoding='utf-8')
    outFile = open(outPath, "w", encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    myMin = 1
    minCase = ""
    myMax = 0
    maxCase = ""
    valueList = []
    for case in data:
        valueList.append((case, data[case]))
        minTuple = min(valueList, key=lambda x: x[1])
        maxTuple = max(valueList, key=lambda x: x[1])
        minCase = minTuple[0]
        myMin = minTuple[1]
        maxCase = maxTuple[0]
        myMax = maxTuple[1]
    print("min:", myMin, minCase)
    print("max:", myMax, maxCase)

    standard_dict = {}
    # 正向指标，标准化结果为 （xi-min）/（max-min）
    if isPositive:
        for case in data:
            ori_value = data[case]
            standard_value = (ori_value - myMin) / (myMax - myMin)
            standard_dict.setdefault(case, standard_value)
    # 负向指标，标准化结果为（max-xi）/（max-min）
    else:
        for case in data:
            ori_value = data[case]
            standard_value = (myMax - ori_value) / (myMax - myMin)
            standard_dict.setdefault(case, standard_value)

    json.dump(standard_dict, outFile, sort_keys=True)
    f.close()
    outFile.close()


if __name__ == '__main__':

    valuesList = [['markLevel.json', 'stdMarkLevel.json', False], ['pyPercent.json', 'stdPyPercent.json', False],
                  ['countLine.json', 'stdCountLine.json', True]]

    for value in valuesList:
        std(value)
