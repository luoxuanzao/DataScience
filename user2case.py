import json

# 把按用户分类的JSON文件转成按题目分类的JSON文件
resPath = 'test_data.json'
outPath = 'cases.json'
f = open(resPath, encoding='utf-8')
f1 = open(outPath, "w", encoding='utf-8')
res = f.read()
data = json.loads(res)
myDict = {}
for user in data:
    print(user)
    cases = data[user]['cases']
    # print("cases:")
    # print(cases)
    for case in cases:
        # print("case:")
        # print(case["case_id"], case["case_type"])
        case["user_id"] = user
        myDict.setdefault(case["case_id"], {"case_id": int(case["case_id"])})
        myDict[case["case_id"]].setdefault("user_records", []).append(case)
        # print(myDict)
        # filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
json.dump(myDict, f1, sort_keys=True)
