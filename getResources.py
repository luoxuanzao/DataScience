import json
import os
import urllib.parse
import urllib.request
import zipfile

# 转换JSON->下载源数据->解压并删除压缩包
# 输入：初始JSON文件路径写于resPath
# 输出：在该py文件同级目录下：1. cases.json 2.cases目录(装载解压后的源数据)

# 转换JSON
# 把按用户分类的JSON文件转成按题目分类的JSON文件
print("Begin:", "user2case")
resPath = 'test_data.json'
# resPath = 'C:/Users/12463/Desktop/test_data.json'
outPath = 'cases.json'
f = open(resPath, encoding='utf-8')
f1 = open(outPath, "w", encoding='utf-8')
res = f.read()
data = json.loads(res)
myDict = {}
for user in data:
    print(user)
    cases = data[user]['cases']
    for case in cases:
        case["user_id"] = user
        myDict.setdefault(case["case_id"], {"case_id": int(case["case_id"])})
        myDict[case["case_id"]].setdefault("user_records", []).append(case)
json.dump(myDict, f1, sort_keys=True)
f.close()
f1.close()
print("Finish:", "user2case")

# 下载源数据
print("Begin:", "downloadCases")
resPath = 'cases.json'
dir_name = "cases"
f = open(resPath, encoding='utf-8')
res = f.read()
data = json.loads(res)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
case_num = len(data)
print(case_num)
# 遍历每一道题目
count = 0
for case in data:
    print("Begin:", case)
    # 每一道题目都创建一个以该题id为名的文件夹
    if not os.path.exists(dir_name + "/" + case):
        os.makedirs(dir_name + "/" + case)
    users_records = data[case]["user_records"]
    # 遍历该道题目的每一个用户
    for user_records in users_records:
        upload_records = user_records["upload_records"]
        final_score = user_records["final_score"]
        # 遍历该道题目的该用户的每一个提交记录，取最高分的那一次
        for upload_record in upload_records:
            if upload_record["score"] == final_score:
                valid_record = upload_record
                filename = urllib.parse.unquote(os.path.basename(valid_record["code_url"]))
                urllib.request.urlretrieve(valid_record["code_url"], "./" + dir_name + "/" + case + "/" + filename)
                break
    print("Finish:", case)
    count = count + 1
    progress = round((count / case_num) * 100, 2)
    print("Progress:", progress, "%")
f.close()
print("Finish: ", "downloadCases")

# 解压并删除压缩包
print("Begin:", "unzip and delete")
resPath = 'cases.json'
dir_name = "cases"
# dir_name = "C:/Users/12463/Desktop/cases/cases"
errPath = "unzipError.txt"
if os.path.exists(errPath):
    os.remove(errPath)
errFile = open(errPath, "a", encoding='utf-8')
f = open(resPath, encoding='utf-8')
res = f.read()
data = json.loads(res)


def unzipFile():
    f = open(resPath, encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    # 遍历每一个题目
    for case in data:
        # 打开对应题目的文件夹
        print(case)
        case_dir_str = "./" + dir_name + "/" + case
        results_dir_str = case_dir_str + "/" + "results"

        # 遍历该题目的每一个用户记录，解压每一个用户记录到该目录下的results文件夹中，解压第一层
        case_dir = os.listdir(case_dir_str)
        for user_record in case_dir:
            if user_record[-4:] == ".zip":
                try:
                    user_record_z = zipfile.ZipFile(case_dir_str + "/" + user_record, "r")
                    user_record_z.extractall(results_dir_str)
                except Exception:
                    errFile.write(case_dir_str + "/" + user_record + "\n")
        # 解压第二层
        results_dir = os.listdir(results_dir_str)
        for result in results_dir:
            if result[-4:] == ".zip":
                result_z = zipfile.ZipFile(results_dir_str + "/" + result, "r")
                result_z.extractall(results_dir_str + "/" + result[:-4])


# 删除解压后的文件
def deleteFile():
    f = open(resPath, encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    # 遍历每一个题目
    for case in data:
        # 删除第一层的压缩文件

        print(case)
        case_dir_str = dir_name + "/" + case
        zipfiles = os.listdir(case_dir_str)
        for zip in zipfiles:
            if zip[-4:] == ".zip":
                path = case_dir_str + "/" + zip  # 文件路径
                if os.path.exists(path):  # 如果文件存在
                    # 删除文件，可使用以下两种方法。
                    os.remove(path)
                    # os.unlink(path)
                else:
                    print('no such file')  # 则返回文件不存在

        results_dir_str = case_dir_str + "/" + "results"
        results_dir = os.listdir(results_dir_str)
        for result in results_dir:
            if result[-4:] == ".zip":
                path = results_dir_str + "/" + result  # 文件路径
                if os.path.exists(path):  # 如果文件存在
                    # 删除文件，可使用以下两种方法。
                    os.remove(path)
                    # os.unlink(path)
                else:
                    print('no such file')  # 则返回文件不存在


unzipFile()
deleteFile()
print("Finish:", "unzip and delete")
print("Done!")
