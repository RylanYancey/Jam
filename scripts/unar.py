import subprocess
import sys

import utility

import subprocess
import sys

import utility

project = ""
try:
    project = sys.argv[1]
except:
    print("Cannot unarchive project! No Archive name provided!")
    exit()

if (not utility.archive_exists(project)):
    print("Cannot unarchive project! Archive does not exist!")
    exit()

if (utility.project_exists(project)):
    print("Cannot unarchive project! Project already exists with this name!")
    exit()

dir = utility.path_to_jam()

ppath = dir + 'projects/' + project
apath = dir + 'archive'

subprocess.run(["mv", apath, ppath])

utility.unarchive_project(project)