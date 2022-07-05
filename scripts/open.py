
import subprocess
import sys

import utility;

project = ""
try:
    project = sys.argv[1]
except:
    project = utility.last_accessed_project()

pwd = utility.path_to_jam()

project_dir =  pwd + 'projects/' + project

if (not utility.project_exists(project)):
    print("Cannot open project. Project does not exist.")
    exit()

ide_cmd = utility.get_ide_cmd()

subprocess.call(ide_cmd, shell=True, cwd=project_dir)

utility.update_last_access_time(project)