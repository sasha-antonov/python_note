import os
import re

def dfile(file_r):
    text_l = []
    path_s = ""
    path_l = []

    path_s = str(file_r)
    path_s = path_s[1:-4]
    path_l = list(path_s)
    for i in range(len(path_l)):
        if path_l[i] == '\\':
            path_l[i] = '/'

    s = len(path_l)
    for i in range(len(path_l)):
        if path_l[s-1-i:s-i] == ['/']:
            path_l[s-1-i:s-i] = [":"]
            break

    path_s = "".join(path_l)
    text_l.append(path_s)

    file = open(file_r, 'r')
    for line in file:
        if(line[-1:] == "\n"):
            text_l.append(line[:-1])
        else:
            text_l.append(line)

    file.close()
    return text_l


def fof():
    path_l = []
    for top, dirs, files in os.walk('.\ROOT'):
        for nm in files:
            path_l.append(os.path.join(top, nm))
    return path_l
	
	
def_file = []
test_l = []

f = open("menu.txt", "w")

path_l = fof()
for i in range(len(path_l)):
    print(path_l[i])
    def_file.append(dfile(str(path_l[i])))

for j in range(len(def_file)):
    test_l = def_file[j]
    for k in range(len(test_l)):
        f.write(str(test_l[k]))
        f.write('\n')

    f.write('\n')

f.close()
