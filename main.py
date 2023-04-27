import json
from PIL import Image
import os.path
n = 200 #72218
aspect_ratios = set()
click = -1
for i in range (0, n+1):
    name_json = 'unique_uis/combined/' + str(i) + '.json'
    name_jpg = 'unique_uis/combined/' + str(i) + '.jpg'
    if (os.path.exists(name_json)):
        with open(name_json, "r") as my_file:
            cur_json = my_file.read()
        current = json.loads(cur_json)
        if (current["activity"]["root"]["clickable"] == False):
            click += 1
    # a = current["activity"]["root"]["bounds"][2]
    # b = current["activity"]["root"]["bounds"][3]
    # res = a/b
    # aspect_ratios.add(round(res, 4))
    if (os.path.exists(name_jpg)):
        img = Image.open(name_jpg)
        #print(img.size)
        width, height = img.size
        res = width / height
        aspect_ratios.add(round(res, 4))
print('отношения сторон: ', end = '')
print(aspect_ratios)
print ('неинтерактивных скринов: ' + str(click))
