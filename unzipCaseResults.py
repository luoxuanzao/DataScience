import zipfile
import json
import os

resPath = 'cases.json'
dir_name = "C:/Users/12463/Desktop/cases/cases"


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
                print(user_record)
                user_record_z = zipfile.ZipFile(case_dir_str + "/" + user_record, "r")
                user_record_z.extractall(results_dir_str)
        # 解压第二层
        results_dir = os.listdir(results_dir_str)
        for result in results_dir:
            if result[-4:] == ".zip":
                print(result)
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
        case_dir_str =  dir_name + "/" + case
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


# unzipFile()
deleteFile()
