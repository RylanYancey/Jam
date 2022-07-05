import subprocess
import sys

import utility

project  = ""
template = ""
makefile = ""
category = ""

try:
    project = sys.argv[1]
except:
    print(project)
    print("Jam Error: No Project Name was Provided!")
    exit()

if (utility.project_exists(project)):
    print("Project with that name already exists!")
    exit()

try:
    category = sys.argv[2]
except:
    category = "c++"
finally:
    if (not utility.category_exists(category)):
        print("Invalid category provided!")
        exit()

try:
    template = sys.arv[3]
except:
    template = "default"
finally:
    if (not utility.template_exists(template)):
        print("Invalid Template provided!")
        exit()

try:
    makefile = sys.arv[4]
except:
    makefile = "default"
finally:
    if (not utility.makefile_exists(makefile)):
        print("Invalid Makefile provided!")
        exit()

pwd = utility.path_to_jam()

tpath = pwd + 'templates/' + template
mpath = pwd + 'makefiles/' + makefile
ppath = pwd + 'projects/'  + project

ide_cmd = utility.get_ide_cmd()

subprocess.run(['mkdir', ppath])
subprocess.run(['cp', '-r', mpath + '/.', tpath + '/.', ppath + '/'])
subprocess.call(ide_cmd, shell=True, cwd=ppath)

utility.add_new_project(project, category)
