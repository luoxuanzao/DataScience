import json

f = open("countLine.json")
f1 = open("linesRank.json", "w", encoding="utf-8")

lines = json.load(f)
a = sorted(lines.items(), key=lambda x: x[1], reverse=True)
#
# print(lines)
# print(a)
length = len(a)
count = 1
j = 1
result = {}
temp = {"lines": a[0][1], "difficulty": 5}
result[a[0][0]] = temp
for i in range(1, 6):
    num = length * i / 5
    # print(num)
    while j < length and count < num:
        temp = {"lines": a[j][1], "difficulty": 6 - i}
        # print(a[j], "难度：", 6 - i)
        result[a[j][0]] = temp
        if a[j][1] < a[j - 1][1]:
            count += 1
        j += 1
print(result)
json.dump(result, f1, sort_keys=False)
