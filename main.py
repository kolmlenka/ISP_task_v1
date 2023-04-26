import json
n = 30 #72218
aspect_ratios = set()
click = -1
for i in range (0, n+1):
    name = 'unique_uis/combined/' + str(i) + '.json'
    #print(name)
    with open(name, "r") as my_file:
        cur_json = my_file.read()
    current = json.loads(cur_json)
    a = current["activity"]["root"]["bounds"][2]
    b = current["activity"]["root"]["bounds"][3]
    res = a/b
    aspect_ratios.add(round(res, 4))
    #print(current["activity"]["root"]["clickable"])
    if (current["activity"]["root"]["clickable"] == False):
        click += 1
print('отношения сторон: ', end = '')
print(aspect_ratios)
print ('неинтерактивных скринов: ' + str(click))
