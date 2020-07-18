import json
import urllib.request, urllib.parse
import os

resPath = 'cases.json'
dir_name = "cases"
f = open(resPath, encoding='utf-8')
res = f.read()
data = json.loads(res)
if not os.path.exists(dir_name):
    print("not exist Dir:" + dir_name + " create it!")
    os.makedirs(dir_name)
# 遍历每一道题目
for case in data:
    print(case)
    # 每一道题目都创建一个以该题id为名的文件夹
    if not os.path.exists(dir_name + "/" + case):
        print("not exist create")
        os.makedirs(dir_name + "/" + case)
    print("exist")
    users_records = data[case]["user_records"]
    print(users_records)
    # 遍历该道题目的每一个用户
    for user_records in users_records:
        print(user_records)
        upload_records = user_records["upload_records"]
        final_score = user_records["final_score"]
        # 遍历该道题目的该用户的每一个提交记录，取最高分的那一次
        for upload_record in upload_records:
            if upload_record["score"] == final_score:
                valid_record = upload_record
                print(valid_record)
                filename = urllib.parse.unquote(os.path.basename(valid_record["code_url"]))
                print(filename)
                urllib.request.urlretrieve(valid_record["code_url"], "./" + dir_name + "/" + case + "/" + filename)
                break
