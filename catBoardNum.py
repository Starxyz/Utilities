import re
import json


fileName = 'id_bd.h'


def findUniqueBoard(fileName):
    with open(fileName) as f:
        txt = f.read()
        # items = re.findall(r'P[A-Z]\d+[^\s]+', txt)
        items = re.findall(r'P[A-Z]\d+', txt)
        # for _ in items:
        #     print(_)

        # print(items)
        # print(len(set(items)))
        print(len(items))
        # unique = set([x for x in items if items.count(x) > 1])
        unique = set([x for x in items if items.count(x) > 1])
        print(unique)
        print(len(unique))
        dictRes = {}
        # for _ in unique:
        #     dictRes[_].append()

        return unique


unique = findUniqueBoard(fileName)

dicts = {}
set1 = set()
with open(fileName) as f:
    l = f.readlines()
    i = 0
    for x in unique:
        if x not in dicts:
            dicts[x] = set()
        for _ in l:
            if re.search(x, _):
                set1.add(_)
                dicts[x].add(_)
                i += 1
                # dicts[x].append(_)
        # print(dicts)
    print(len(set1))
    print(len(dicts))

# js = json.dumps(dicts)
# print(js)
with open('res.txt', 'w') as f:
    for k, v in dicts.items():
        # print(dicts[k])
        print('{key}:{value}'.format(key=k, value=v))
        f.write('{key}:{value}\n'.format(key=k, value=v))
#     f.write(str(dicts))
