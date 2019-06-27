import os
from shutil import copy2
import random

filepaths = []
file = None
linecount = 0
randomsongs = []
randomcount = 0

for root, dirs, files in os.walk('D:\\M'):
    if files:
        for i in files:
            if i.endswith('.mp3'):
                filepaths.append(os.path.join(root, i))

try:
    file = open('paths.txt', 'r+')
except:
    file = open('paths.txt', 'a')

with open('paths.txt', 'r') as f:
    linecount = sum(1 for _ in f)

file = open('paths.txt', 'r+')

if (linecount <= 0):
    for i in filepaths:
        file.write(i+'\n')
else:
    print()

while randomcount < 150:
    number = random.randint(0, linecount-1)

    if number not in randomsongs:
        randomsongs.append(number)
        randomcount += 1

for i in randomsongs:
    copy2(filepaths[i],'C:\\Users\\Juan.DESKTOP-HA52B1R\\Desktop\\songs')
