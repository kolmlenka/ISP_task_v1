import json
from PIL import Image
import os.path
import matplotlib.pyplot as plt

n = 1000 #72218
aspect_ratios = set()
count = 0
y_list = [] #list that consists of the depths of trees
x_list = [] #list that consists of the numbers of trees

def deepth(dictionary, d=0):
    for k in dictionary.keys():
        if type(dictionary[k]) is (str or bool):
            d += 1
        elif type(dictionary[k]) is (dict or list):
            deepth(dictionary[k], d)
    return d

def clickable(dictionary, flag=False):
    for k in dictionary.keys():
        if (k == "clickable") and (dictionary[k] is True):
            print(k, dictionary[k])
            flag = True
            break
        elif type(dictionary[k]) is dict:
            clickable(dictionary[k], flag)
    return flag

for i in range (0, n+1):
    name_json = 'unique_uis/combined/' + str(i) + '.json'
    name_jpg = 'unique_uis/combined/' + str(i) + '.jpg'

    if (os.path.exists(name_json)):
        with open(name_json, "r") as my_file:
            cur_json = my_file.read()
        current = json.loads(cur_json)

        x_list += [i]
        y_list += [deepth(current, d=0)]

        if clickable(current, flag=False) is True:
            count += 1

    if (os.path.exists(name_jpg)):
        img = Image.open(name_jpg)
        width, height = img.size
        res = width / height
        aspect_ratios.add(round(res, 4))

print('отношения сторон: ', end = '')
print(aspect_ratios)

plt.title('График распределения глубин UI деревьев', fontsize = 14, color = 'black')
plt.xlabel('Номер дерева')
plt.ylabel('Глубина дерева')
plt.plot(x_list, y_list)
plt.grid()
plt.show()

print ('интерактивных скринов: ' + str(count))
