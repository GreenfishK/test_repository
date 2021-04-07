#!/bin/sh

# Variables
# Actually $CONDA_PREFIX was intended to be used here but it seems that it is overwritten with $BUILD_PREFIX.
dir_in_conda=$SYS_PREFIX/lib/python3.8/site-packages/$PKG_NAME 

# Install
echo "Start installation"
# mkdir $dir_in_conda
# cp -RT $RECIPE_DIR/$PKG_NAME $dir_in_conda
