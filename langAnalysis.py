import json
import os

resPath = "cases.json"
outputPath = "langAnalysis.json"
pyPercentPath = "pyPercent.json"
dir_name = "cases"
f = open(resPath, encoding='utf-8')
outputFile = open(outputPath, "w", encoding='utf-8')
pyPercentFile = open(pyPercentPath, "w", encoding='utf-8')

res = f.read()
data = json.loads(res)
result_dict = {}
pyPercent_dict = {}
no_py_count = 0
for case in data:
    print(case)
    result_dict.setdefault(case, {"case_id": int(case)})
    case_dict = result_dict[case]
    case_dict["case_num"] = 0
    case_dict["languages"] = {}
    case_dir_str = os.path.join(dir_name, case)
    result_dir_str = os.path.join(case_dir_str, "results")
    result_dir = os.listdir(result_dir_str)
    for result in result_dir:
        result_str = os.path.join(result_dir_str, result)
        if os.path.isdir(result_str):
            properties_str = os.path.join(result_str, "properties")
            properties_file = open(properties_str, encoding='utf-8')
            properties_json = json.loads(properties_file.read())
            lang = properties_json["lang"]
            if lang not in case_dict["languages"]:
                lang_count = 1
            else:
                lang_count = case_dict["languages"][lang] + 1
            case_dict["languages"][lang] = lang_count
            case_dict["case_num"] = case_dict["case_num"] + 1

    py_count = 0
    for language in case_dict["languages"]:
        if language == "Python3" or language == "Python":
            py_count = py_count + case_dict["languages"][language]
        else:
            no_py_count = no_py_count + case_dict["languages"][language]
    py_percent = py_count / case_dict["case_num"]
    case_dict["py_percent"] = py_percent
    pyPercent_dict.setdefault(case, py_percent)
result_dict.setdefault("not_py_count", no_py_count)

json.dump(result_dict, outputFile, sort_keys=True)
json.dump(pyPercent_dict,pyPercentFile,sort_keys=True)
