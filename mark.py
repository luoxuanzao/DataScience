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
                startMarkSum.append(records[len(records)-1]["score"])
            else:
                startMarkSum.append(0)
            peopleNum.append(1)
        else:
            index = questionId.index(caseId)
            finalMarkSum[index] += case['final_score']
            if len(records) > 0:
                startMarkSum[index] += records[len(records)-1]["score"]
            peopleNum[index] += 1
finalMarkAverage = []
startMarkAverage = []
for i in range(0, len(questionId)):
    finalMarkAverage.append(finalMarkSum[i] / peopleNum[i])
    startMarkAverage.append(startMarkSum[i] / peopleNum[i])
# finalMarkAverage.sort()
startMarkAverage.sort()
print(len(finalMarkAverage))
# print(finalMarkAverage)
# print(startMarkAverage)
# plt.plot(finalMarkAverage, color='red')
plt.plot(startMarkAverage, color='blue')
plt.show()
