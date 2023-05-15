import json
from PIL import Image
import os.path
import matplotlib.pyplot as plt

n = 1000 #72218
aspect_ratios = set()
count = 0
y_list = [] #список в котором собираю все глубины деревьев
x_list = [] #список в котором номера деревьев

def deepth(dictionary, some_list = []):
    for k in dictionary.keys():
        if type(dictionary[k]) is (str or bool):
            some_list += ['1']
        elif type(dictionary[k]) is (dict or list):
            deepth(dictionary[k], some_list)
    return len(some_list)

def clickable(dictionary, click = set()):
    for k in dictionary.keys():
        if k == 'clickable':
            click.add(dictionary[k])
        elif type(dictionary[k]) is (dict or list):
            clickable(dictionary[k], click)
    if False in click:
        return 1
    else:
        return 0

for i in range (0, n+1):
    name_json = 'unique_uis/combined/' + str(i) + '.json'
    name_jpg = 'unique_uis/combined/' + str(i) + '.jpg'

    if (os.path.exists(name_json)):
        with open(name_json, "r") as my_file:
            cur_json = my_file.read()
        current = json.loads(cur_json)

        x_list += [i]
        y_list += [deepth(current, some_list = [])]
        #print(deepth(current, some_list = []))

        count += clickable(current, click = set())

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

print ('неинтерактивных скринов: ' + str(count))
