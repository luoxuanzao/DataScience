import zipfile
import json
import os

resPath = 'cases.json'
dir_name = "cases"
errPath = "unzipError.txt"
if os.path.exists(errPath):
    os.remove(errPath)
errFile = open(errPath, "a", encoding='utf-8')
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
                errFile.write(case_dir_str+"/"+user_record+"\n")
    # 解压第二层
    results_dir = os.listdir(results_dir_str)
    for result in results_dir:
        if result[-4:] == ".zip":
            result_z = zipfile.ZipFile(results_dir_str + "/" + result, "r")
            result_z.extractall(results_dir_str + "/" + result[:-4])

