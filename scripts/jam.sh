#!/bin/bash

path=$(dirname "$(readlink -f "$0")")
python3 "$path""/""$1".py $2 $3 $4 $5
