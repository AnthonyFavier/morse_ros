#! /usr/bin/env sh

# add resources of current package to morse
export MORSE_RESOURCE_PATH=$MORSE_RESOURCE_PATH:`rospack find morse_ros`/blender_files

# start morse with given scenario
morse run -g 1280x720 $1
