import subprocess
import sys

import utility

project = ""

try:
    project = sys.argv[1]
except:
    print("Jam Error: Must provide name of project to remove!")
    exit()

if (not utility.project_exists(project)):
    print("Jam Error: Cannot remove project. Project does not exist.")
    exit()

pwd = utility.path_to_jam()

subprocess.run(["rm", "-rf", pwd + 'projects/' + project])

utility.rm_from_json(project)