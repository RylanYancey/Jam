import subprocess
import sys
from collections import defaultdict

import utility

# jam show [OPTIONS] [CATEGORIES]
# jam show -p c++ 
# jam show -a mpi
# jam show -p 

options = "-p"
try:
    options = sys.argv[1]
except:
    pass

category = ""
try:
    category = sys.argv[2]
except:
    pass

if (category != ""):
    if (not utility.category_exists(category)):
        print("Cannot display category. Invalid.")
        exit()

data = {}
if (options == "-a"):
    data = utility.get_key("ARCHIVE")
else:
    data = utility.get_key("PROJECTS")

dictbycat = defaultdict(list)

for p in data:
    dictbycat[p[2]].append((p[0], p[1]))

for v in dictbycat.values():
    v = sorted(v, key=lambda x: x[1])

if (category == ""):
    for k in dictbycat.keys():
        print(k + ":")
        for v in dictbycat[k]:
            print("     " + v[0])
        print(" ")

else:
    print(category + ": ")
    for v in dictbycat[category]:
        print("     " + v[0])
    print(" ")
