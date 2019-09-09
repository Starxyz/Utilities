import sys

file_path = sys.argv[1]
print(sys.argv[0])

with open('test.h', 'r') as f:
    text = f.read()
    # print(text)
    # print(text.replace('_', ' '))
    with open("res.txt", 'w') as wf:
        wf.write(text.replace('_', ' '))
