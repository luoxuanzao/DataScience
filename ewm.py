import json
import math


# 熵权法计算每个指标的权重

def get_entropy(p_dict):
    count = len(p_dict)
    k = 1 / math.log(count)
    mySum = 0
    for case in p_dict:
        mySum = mySum + p_dict[case] * math.log(p_dict[case])
    entropy = -1 * k * mySum
    return entropy


if __name__ == '__main__':

    stdPyPercentPath = 'stdPyPercent.json'
    stdMarkLevelPath = 'stdMarkLevel.json'
    stdCountLinePath = 'stdCountLine.json'

    stdPyPercent = json.loads(open(stdPyPercentPath, encoding='utf-8').read())
    stdMarkLevel = json.loads(open(stdMarkLevelPath, encoding='utf-8').read())
    stdCountLine = json.loads(open(stdCountLinePath, encoding='utf-8').read())

    alphaPy = float(input("请输入python占比的主观权重："))
    alphaMark = float(input("请输入平均得分的主观权重："))
    alphaCountLine = float(input("请输入平均代码行数的主观权重："))
    indexNum = 3
    if alphaPy < 0 or alphaMark < 0 or alphaCountLine < 0:
        print("请保证主观权重非负！")
        quit()
    sumAlpha = alphaPy + alphaMark + alphaCountLine
    alphaPy = alphaPy / sumAlpha
    alphaMark = alphaMark / sumAlpha
    alphaCountLine = alphaCountLine / sumAlpha
    print("主观权重：", "Py:", alphaPy, "Mark:", alphaMark, "CountLine:", alphaCountLine)
    pPyPercent = {}
    pMark = {}
    pCL = {}
    sumPyPercent = 0
    sumMark = 0
    sumCL = 0
    for i in stdPyPercent:
        stdPyPercent[i] = stdPyPercent[i] * alphaPy + (1 - alphaPy)
        stdMarkLevel[i] = stdMarkLevel[i] * alphaMark + (1 - alphaMark)
        stdCountLine[i] = stdCountLine[i] * alphaCountLine + (1 - alphaCountLine)
        sumPyPercent = sumPyPercent + stdPyPercent[i]
        sumMark = sumMark + stdMarkLevel[i]
        sumCL = sumCL + stdCountLine[i]

    for i in stdPyPercent:
        pPyPercent[i] = stdPyPercent[i] / sumPyPercent
        pMark[i] = stdMarkLevel[i] / sumMark
        pCL[i] = stdCountLine[i] / sumCL

    ePyPercent = get_entropy(pPyPercent)
    eMark = get_entropy(pMark)
    eCL = get_entropy(pCL)
    print("信息熵：", "Py:", ePyPercent, "Mark:", eMark, "CountLine:", eCL)

    sumEntropy = ePyPercent + eMark + eCL
    weightPyPercent = (1 - ePyPercent) / (3 - sumEntropy)
    weightMark = (1 - eMark) / (3 - sumEntropy)
    weightCountLine = (1 - eCL) / (3 - sumEntropy)

    print("最终权重：", "Py:", weightPyPercent, "Mark:", weightMark, "CountLine:", weightCountLine)
