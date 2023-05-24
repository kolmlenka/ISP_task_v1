import json
import imagesize
import os.path
import matplotlib.pyplot as plt

n = 100  # 72218
aspect_ratios = set()
count = 0
list_of_depths = []


def deepth(dictionary, d=None):
    if not d:
        d = 0
    for k in dictionary.keys():
        if k == "children":
            d += 1
            for j in range(len(dictionary[k])):
                d += deepth(dictionary[k][j])
        elif type(dictionary[k]) is dict:
            d += deepth(dictionary[k])
    return d


def depth(node):
    if not node:
        return 1
    return max(depth(d) for d in node["children"])


def test(node):
    if not node:
        return 1
    for d in range(len(node["children"])):
        return max(test(node["children"][d])) + 2


def clickable(dictionary, flag=None):
    if not flag:
        flag = False
    for k in dictionary.keys():
        if (k == "clickable") and (dictionary[k] is True):
            return True
        elif type(dictionary[k]) is dict:
            flag = clickable(dictionary[k], flag)
        elif k == "children":
            for j in range(len(dictionary[k])):
                flag = clickable(dictionary[k][j], flag)
    return flag


for i in range(0, n + 1):
    name_json = "unique_uis/combined/" + str(i) + ".json"
    name_jpg = "unique_uis/combined/" + str(i) + ".jpg"

    if os.path.exists(name_json):
        with open(name_json, "r") as my_file:
            cur_json = my_file.read()
        current = json.loads(cur_json)

        list_of_depths += [test(current["activity"]["root"])]

        if clickable(current) is True:
            count += 1

    if os.path.exists(name_jpg):
        width, height = imagesize.get(name_jpg)
        res = width / height
        aspect_ratios.add(round(res, 4))

print("отношения сторон: ", end="")
print(aspect_ratios)

print("интерактивных скринов: " + str(count))

fig = plt.figure(figsize=(6, 4))
x = fig.add_subplot()
x.hist(list_of_depths, 25)
x.grid()
plt.show()
