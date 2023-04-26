import json
n = 10#72218
for i in range (0, n+1):
    name = 'unique_uis/combined/' + str(i) + '.json'
    print(name)
    with open(name, "r") as my_file:
        cur_json = my_file.read()
    current = json.loads(cur_json)

