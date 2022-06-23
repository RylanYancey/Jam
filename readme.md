
## Important! Note for Existing Users!

Before updating Jam by using `git clone`, be sure to backup your `Jam/projects/` folder in a location other than Jam, to avoid your projects being lost. 

# WHAT IS JAM?

Jam is a Project Manager for C++ beginners. 

Jam's main features are:

- Template System
- Makefile System
- Project Loader
- Archiver

Jam currently only supports VSCode by default, but it is very easy to change it to work for Emacs or some other text editor by changing a single variable.

In the future, Jam may have the ability to sort projects by most recent, view git information, have an attribute system for classifying projects, and support other languages. For now, Jam is very basic. 

# JAMS' PRIMARY COMMANDS

## Jam man

Opens the manual for Jam in the terminal.

## Jam new \<filename> \<template name> \<makefile name>

Used to create a new project within Jam. It is stored in the Jam/projects folder.

Options:

\<filename>: This field is the name you want your project to have. Cannot be left blank. 

\<template name>: The name of the template you want to use. Templates are stored in Jam/templates. If left blank, the 'default' template will be used. 

\<makefile name>: The name of the makefile you want to use. Makefiles are stored in Jam/makefiles. If left blank, the 'default' makefile will be used. 

Note: Jam new will also initialize an empty repository using `git init` in this new project.

## Jam add \<path/to/file>

Used to move an existing project into Jam. 

IMPORTANT NOTE: When using Jam add, make certain you are in the home directory. The path supplied should be from the home directory. For example, Jam add ~/projects/project_to_move

\<path/to/file>: The absolute path from the home directory (~/) to the file you want to move into Jam. 

## Jam open \<filename>

Used to open an existing project in VSCode. 

\<filename>: The name of the Jam project. 

## Jam show \<option>

Used to see all of the projects in Jam. 

\<option>: If left blank, it will show all Jam projects. If -a is used, all archived files will be shown. 

## Other:

Jam ar\
Jam unar\
Jam make\
Jam rm

use Jam man to see the docs for these. 

# Installation

Before you start MAKE SURE YOU ARE IN YOUR HOME DIRECTORY!
For the most part, these commands should be copy/paste

1) Clone the repository into your home directory. \
```git clone https://github.com/RylanYancey/Jam.git```

2) Create empty files Jam requires to work (git will delete empty files when pushing)
```
mkdir Jam/projects && mkdir Jam/archive
mkdir Jam/templates/default/header && mkdir Jam/templates/default/bin 
```
3) Delete git repository created in Jam
```
rm -rf ~/Jam/.git
```

4) Set up Jam as as executable
```
chmod u+x Jam/config/Jam.sh
```

5) Create a Bash Alias for Jam
```
touch ~/.bash_aliases && nano ~/.bash_aliases
```
The above opens the Nano text editor.
Paste these lines into .bash_aliases:
```
# Jam C++ Project Manager
alias Jam="bash ~/Jam/config/Jam.sh
```
Close Nano with CNTR+S then CNTR+X

6) Tell Shell Jam is an alias. 
```
source ~/.bash_aliases
```
After doing this, you should now be able to use Jam. If you use `Jam man`, you should see the manual. 

Start using Jam by using Jam new, or Jam add `~/path/to/folder/from/homedir/` to add existing projects.

# Changing Jam to work with Emacs / Vim / other text editors. 

The first step is to identify what command is used to open your text editor. For Emacs, you can just type 'emacs' in the terminal. For Jam, open ~/Jam/config/Jam.sh 

```sh
#!/bin/bash/

OPEN_IDE_COMMAND="code ."

# $1 = Name of project
# $2 = Template to use
# $3 = Name of makefile
function new {
```
^^ At the top of Jam.sh, there is code like this. Change OPEN_IDE_COMMAND to whatever text editor you want to use. For VScode, leave as is, for Emacs, change it to 
```
OPEN_IDE_COMMAND="emacs"
```
# Creating Templates and Makefiles

Feel free to change / remove default templates / makefiles. Jam will work fine with or without them. 

## Template System

Whenever you create a new project, Jam will use one of the templates in the Jam/templates folder. Jam comes included with a default template folder that will work with all 3 of the makefiles included. If you want to make new templates, simply go into the Jam/templates folder, create a new folder, and occupy it with what you want a project to look like when you start it. To make a template the default template, just change the name to 'default'. 

## Makefile System

Makefiles are used to build your project into a binary. By default, Jam comes with 3 makefiles, one for G++, one for MPI, and another for CUDA. They also include documentation within them on how to use them and what they are for. By default, the makefile in the 'default' folder will be used. To create new makefiles, open Jam/makefiles, create a new folder with the name you want, and create your makefile in the folder. 

To change the makefile you are currently using, use the 'Jam make \<filename> \<makefile_name>' command. See Jam man for more details. 
