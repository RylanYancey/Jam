
from os.path import exists
from time import time_ns
import pathlib
import json

def __open_json_data__():
    with open(path_to_jam() + "scripts/config.json") as file:
        return json.load(file)

def __dump_json_data__(data):
    with open(path_to_jam() + "scripts/config.json", 'w') as file:
        json.dump(data, file, indent=4, separators=(',', ' : '))

def get_ide_cmd():
    config = __open_json_data__()
    return config["OPEN_IDE_COMMAND"]

def path_to_jam():
    return str(pathlib.Path(__file__).parent.resolve()).strip('\\n\'').strip('b\'').strip('scripts')

def project_exists(project_name):
    return exists(path_to_jam() + 'projects/' + project_name)

def template_exists(template_name):
    return exists(path_to_jam() + 'templates/' + template_name)

def makefile_exists(makefile_name):
    return exists(path_to_jam() + 'makefiles/' + makefile_name)

def archive_exists(archive_name):
    return exists(path_to_jam() + 'archive/' + archive_name)

def category_exists(category):
    data = __open_json_data__()
    for c in data["CATEGORIES"]:
        if (c == category):
            return True
    return False

def get_key(key):
    data = __open_json_data__()
    return data[key]

def add_new_project(project_name, category):
    data = __open_json_data__()
    rm_from_json(project_name)
    data["PROJECTS"].append([project_name, time_ns(), category])
    __dump_json_data__(data)

def archive_project(project_name):
    data = __open_json_data__()
    for i, p in enumerate(data["PROJECTS"]):
        if (p[0] == project_name):
            data["ARCHIVE"].append(p)
            data["PROJECTS"].pop(i)
            break
    __dump_json_data__(data)

def unarchive_project(archive_name):
    data = __open_json_data__()
    for i, p in enumerate(data["ARCHIVE"]):
        if (p[0] == archive_name):
            data["PROJECTS"].append(p)
            data["ARCHIVE"].pop(i)
            break
    __dump_json_data__(data)

def update_last_access_time(project_name):
    data = __open_json_data__()
    found = False
    for p in data["PROJECTS"]:
        if (p[0] == project_name):
            p[1] = time_ns()
            found = True
            break

    if (found == False):
        add_new_project(project_name, "c++")

    __dump_json_data__(data)

def last_accessed_project():
    data = __open_json_data__()
    temp = ["", 0, ""]
    for p in data["PROJECTS"]:
        if (p[1] > temp[1]):
            temp = p
    return temp[0]

def rm_from_json(project_name):
    data = __open_json_data__()
    for p in data["PROJECTS"]:
        if (p[0] == project_name):
            data["PROJECTS"].remove(p)
    __dump_json_data__(data)

def all_projects():
    data = __open_json_data__()
    return data["PROJECTS"]
