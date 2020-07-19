import json
import matplotlib.pyplot as plt

f = open('test_data.json', encoding="utf-8")
res = f.read()
data = json.loads(res)
# questionId为题目编号
# finalMarkSum为最终得分的总和
# startMarkSum为初始得分的总和
# peopleNum为答题人数
questionId = []
finalMarkSum = []
startMarkSum = []
peopleNum = []
for key in data.keys():
    student = data[key]
    cases = student["cases"]
    for case in cases:
        caseId = case["case_id"]
        records = case["upload_records"]
        if questionId.count(caseId) == 0:
            questionId.append(caseId)
            finalMarkSum.append(case["final_score"])
            if len(records) > 0:
                startMarkSum.append(records[len(records) - 1]["score"])
            else:
                startMarkSum.append(0)
            peopleNum.append(1)
        else:
            index = questionId.index(caseId)
            finalMarkSum[index] += case['final_score']
            if len(records) > 0:
                startMarkSum[index] += records[len(records) - 1]["score"]
            peopleNum[index] += 1
finalMarkAverage = {}
# finalMarkAverageList为最终平均得分的数组形式，用于画出折线图，观察得分的分布情况
finalMarkAverageList = []
for i in range(0, len(questionId)):
    finalMarkAverage[questionId[i]] = finalMarkSum[i] / peopleNum[i]
    finalMarkAverageList.append(finalMarkSum[i] / peopleNum[i])
finalMarkAverage = sorted(finalMarkAverage.items(), key=lambda x: x[1], reverse=False)
print(len(finalMarkAverage))
# print(finalMarkAverage)
finalMarkAverageList.sort()
# plt.plot(finalMarkAverageList, color='red')
# plt.plot(startMarkAverage, color='blue')
# plt.show()


# for i in range(1, len(finalMarkAverageList)):
#    if finalMarkAverageList[i - 1] < 80 and finalMarkAverageList[i] >= 80:
#        print("80:")
#        print(i)
#    elif finalMarkAverageList[i - 1] < 85 <= finalMarkAverageList[i]:
#        print("85:")
#        print(i)
#    elif finalMarkAverageList[i - 1] < 90 <= finalMarkAverageList[i]:
#        print("90:")
#        print(i)
#    elif finalMarkAverageList[i - 1] < 95 <= finalMarkAverageList[i]:
#        print("95:")
#        print(i)


# 根据最终得分的情况对题目难度进行评级
# 得分为1——5，1为最简单，5为最难
# 第535题以后所有题目的得分都为100.0，占全部的40%，他们的难度为1
# 得分在80以下的为2，80——85之间为2，85——90之间为19，90——95之间为81，95——100之间为431
# 占比分别为0.002，0.002，0.021，0.091，0.488
# 在剩余60%的题目按照5%，10%，20%，25%归类为难度为5，4，3，2
# 题目数量分别为44，88，179，224
# markDifficulty表示根据得分所评价的题目难度
markDifficulty = {}
for i in range(len(finalMarkAverage)):
    if i < 44:
        markDifficulty[finalMarkAverage[i][0]] = 5
    elif i < 132:
        markDifficulty[finalMarkAverage[i][0]] = 4
    elif i < 311:
        markDifficulty[finalMarkAverage[i][0]] = 3
    elif i < 535:
        markDifficulty[finalMarkAverage[i][0]] = 2
    else:
        markDifficulty[finalMarkAverage[i][0]] = 1
print(markDifficulty)

outPath = 'markLevel.json'
outFile = open(outPath, "w", encoding='utf-8')
json.dump(markDifficulty, outFile, sort_keys=True)
