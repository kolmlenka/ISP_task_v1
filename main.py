import json
from PIL import Image
import os.path

n = 2 #72218
aspect_ratios = set()
click = 0

def deepth(dictionary, some_list = []):
    for k in dictionary.keys():
        if type(dictionary[k]) is (str or bool):
            some_list += ['1']
        elif type(dictionary[k]) is (dict or list):
            deepth(dictionary[k], some_list)
    return len(some_list)

for i in range (0, n+1):
    name_json = 'unique_uis/combined/' + str(i) + '.json'
    name_jpg = 'unique_uis/combined/' + str(i) + '.jpg'
    if (os.path.exists(name_json)):
        with open(name_json, "r") as my_file:
            cur_json = my_file.read()
        current = json.loads(cur_json)
        print(deepth(current, some_list = []))
        
        #flag = True
        #clickable = set()
        #while flag == True:
            #print(current["activity"]["root"]["clickable"])
            #clickable.add(current["activity"]["root"]["clickable"])
            #for i in range(len(current["activity"]["root"]["children"])):
                #print(current["activity"]["root"]["children"][i]["clickable"])
                #clickable.add(current["activity"]["root"]["children"][i]["clickable"])
                #for i in range(current["activity"]["root"]["children"][i]["children"]):
                    #print(current["activity"]["root"]["children"][i]["children"][])
                    #clickable.add(current["activity"]["root"]["children"][i]["clickable"])
            #flag = False

    if (os.path.exists(name_jpg)):
        img = Image.open(name_jpg)
        width, height = img.size
        res = width / height
        aspect_ratios.add(round(res, 4))
print('отношения сторон: ', end = '')
print(aspect_ratios)
print ('неинтерактивных скринов: ' + str(click))
