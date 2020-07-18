import json
import os


def count_path(path, countcode):
    if os.path.isdir(path):
        file_list = os.walk(path)
        for file_path in file_list:
            x, _, y = file_path
            for i in y:
                if i.split('.')[-1] == 'py':
                    count_path(os.path.join(x, i), countcode)
    if os.path.isfile(path):
        count_code(path, countcode)


def count_code(path, countcode):
    flag = True
    count = 0
    with open(f'{path}', encoding='utf-8') as fr:
        for i in fr:
            if i.startswith('#') and float:
                continue
            if i == '\n' and float:
                continue
            if (i.startswith('\'\'\'') or i.startswith('\"\"\"')) and flag:
                flag = False
                continue
            if (i.startswith('\'\'\'') or i.startswith('\"\"\"')) and not flag:
                flag = True
            count += 1
            countcode[0] += 1
    print(f"当前的文件路径为:{path},代码量为:{count}")


def main():
    result_file = "countLine.json"
    j = open(result_file, "w", encoding='utf-8')
    result = {}
    countcode = [0]
    path = r'C:/Users/12463/Desktop/cases/cases'
    files = os.listdir(path)
    for f in files:
        # print(f)
        newPath = path + "/" + f + "/results"
        answers = os.listdir(newPath)
        # print(answers)
        count = 0
        countcode[0] = 0
        for answer in answers:
            count += 1
            count_path(newPath + "/" + answer + "/main.py", countcode)
        average = countcode[0] / count
        print("平均行数", average)
        result[f] = average
    #
    print(result)
    # print(f"总计代码行数为：{countcode[0]}")
    json.dump(result, j, sort_keys=True)


main()
