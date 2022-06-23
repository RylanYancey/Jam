#!/bin/bash/

OPEN_IDE_COMMAND="code ."

# $1 = Name of project
# $2 = Template to use
# $3 = Name of makefile
function new {

    if [[ -d ./Jam/Projects/"$1" ]]; then
        echo Project already exists\!
    fi

    if [ -z $1 ]; then
        echo Invalid: Must provide a name \for the project\!
        exit
    fi

    local TEMPLATE=$2
    if [ -z $2 ]; then 
        TEMPLATE=default
    fi

    local MAKEFILE=$3
    if [ -z $3 ]; then
        MAKEFILE=default
    fi

    cp -r ./Jam/templates/"$TEMPLATE" ./Jam/projects/
    mv ./Jam/projects/"$TEMPLATE" ./Jam/projects/"$1"

    cp ./Jam/makefiles/"$MAKEFILE"/makefile ./Jam/projects/"$1"/

    cd ./Jam/projects/"$1"
    git init

    eval "$OPEN_IDE_COMMAND"
}

# 1 - the path to the file to copy 
function add {

    if [[ -d ./Jam/projects/"$1" ]]; then
        echo Project already exists \in Projects...
        exit
    fi

    echo Copying from "$1" to Projects...
    cp -R "$1" ./Jam/projects/
}

# 1 - Project
# 2 - Makefile to load
function make {

    if [[ ! -d ./Jam/makefiles/"$2" ]]; then
        echo Makefile does not exist.
        exit
    fi

    if [[ ! -d ./Jam/projects/"$1" ]]; then
        echo Project does not exist.
        exit
    fi

    command rm ./Jam/projects/"$1"/makefile
    cp ./Jam/makefiles/"$2"/makefile ./Jam/projects/"$1"/
}

# 1 - the file name
function ar {

    if [[ ! -d ./Jam/projects/"$1" ]]; then
        echo Project does not exist \in Projects...
        exit
    fi

    if [[ -d ./Jam/archive/"$1" ]]; then
        echo Project already exists \in the Archives
        exit
    fi

    mv ./Jam/projects/"$1" ./Jam/archive/"$1"
}

# 1 - the file name
function rm {

    if [[ -d ./Jam/projects/"$1" ]]; then
        command rm -rf ./Jam/projects/"$1"
        echo Finished\!
    else
        echo $1 does not exist \in Projects.
        echo \if you\'re trying to delete an archived project, you\'ll have to use unar \<filename\> first.
    fi
}

# 1 - the file name
function unar {

    if [[ -d ./Jam/archive/"$1" ]]; then
        mv ./Jam/archive/"$1" ./Jam/projects/
    else
        echo $1 does not exist \in the the archives. 
    fi
}

# 1 - the file name
function open {

    if [[ -d ./Jam/projects/"$1" ]]; then
        cd ./Jam/projects/"$1" && eval "$OPEN_IDE_COMMAND"
    else
        echo $1 not found \in Projects.
    fi
}

# 1 - options
function show {
    path="projects"
    if [ "$1" == "-a" ]; then
        path="archive"
    fi
    
    echo
    for entry in ./Jam/"$path"/*
    do
        echo ${entry##*/}
    done
    echo
}

function man {

    echo
    echo Make sure you are \in your HOME directory. ~/. 
    echo

    echo "Jam new <filename> <template name> <makefile name>"
    echo "    <filename>      => The name of the project you want to make."
    echo "    <template_name> => The name of the template to to load. (if blank it will use the default template)"
    echo "    <makefile_name> => The name of the makefile to load. (if blank it will use the default makefile)"
    echo
    echo "Jam stores makefiles in the Jam/makefiles/ folder and templates in the Jam/templates folder. Feel free to create your own by editing the contents of those files. Keep in mind, the /default folder is the one that will be used if the field is left blank."
    echo
    echo "Jam open <filename>"
    echo "    Opens the specified project file."
    echo
    echo "Jam rm <filename>"
    echo "    Removed the specified project file."
    echo
    echo "Jam ar <filename>"
    echo "    Archives the specified project file. Archived projects cannot be opened."
    echo
    echo "Jam unar <filename>"
    echo "    Brings an Archived file back into Projects, where it can be edited or deleted."
    echo
    echo "Jam add <path/to/file>"
    echo "    Copies a project from another location into Jam."
    echo
    echo "Jam make <filename> <makefile_name>"
    echo "    Changes the makefile of a project to another."
    echo "    <filename>      => The name of the file you want to change the makefile of."
    echo "    <makefile_name> => The name of the makefile you want to change to."
    echo
    echo "Jam show <option>"
    echo "    Shows all of the project names by default."
    echo "    If you use Jam show -a, you can see all archived projects."
    
}

cd ~/
$1 $2 $3 $4
