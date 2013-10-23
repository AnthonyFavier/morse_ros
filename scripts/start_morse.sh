#! /usr/bin/env sh

# display the ROS_PACKAGE_PATH
if [ -n "$ROS_PACKAGE_PATH" ]
then
  echo "Using ROS_PACKAGE_PATH: $ROS_PACKAGE_PATH"
else
  echo ROS_PACKAGE_PATH not set
fi

#TODO: check following while installation
#PYYAML_DIR=$(rospack find morse_pyyaml)
#ROSLIB_DIR=$(rospack find roslib)

#TODO: setup morse as ros package
#MORSE_DIR=$(rospack find morse)

#TODO: setup blender for morse as ros package
#BLENDER_DIR=$(rospack find morse_blender)

# set python version for morse
PYTHON_VERSION=python3.2
if [ -z "$PYTHON3_EXECUTABLE" ]; then
    if which python3.2; then
        PYTHON3_EXECUTABLE=`which python3.2`
    else
        echo "Could not find python3 executable. Please set the environment variable PYTHON3_EXECUTABLE to point to it."
        exit 1
    fi
fi

#PYTHON_INST_DIR=`$PYTHON3_EXECUTABLE -c "import distutils.sysconfig, sys; sys.stdout.write(distutils.sysconfig.get_python_lib(0,0,''))"`
#export PYTHONPATH=$PYYAML_DIR/pyyaml/lib/python3.2/site-packages:$MORSE_DIR/morse/$PYTHON_INST_DIR:$ROSLIB_DIR/src:/usr/$PYTHON_INST_DIR

echo "Using PYTHONPATH: $PYTHONPATH"

if [ -n "$MORSE_BLENDER" ]
then
  echo "Using MORSE_BLENDER: $MORSE_BLENDER"
else
  echo MORSE_BLENDER path-variable not set
fi

# start morse with given scenario
morse run -g 1280x720 $1
#morse check

#TODO:start morse using builder script
#$MORSE_DIR/morse/bin/morse exec $MORSE_DIR/morse/share/examples/morse/scenarii/adapto_rebuild/apartment.py
