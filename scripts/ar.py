import subprocess
import sys

import utility

project = ""
try:
    project = sys.argv[1]
except:
    print("Cannot Archive project! No Project name provided!")
    exit()

if (not utility.project_exists(project)):
    print("Cannot archive project! Project does not exist!")
    exit()

if (utility.archive_exists(project)):
    print("Cannot archive project! Archive already exists with this name!")
    exit()

dir = utility.path_to_jam()

ppath = dir + 'projects/' + project
apath = dir + 'archive'

subprocess.run(["mv", ppath, apath])

utility.archive_project(project)