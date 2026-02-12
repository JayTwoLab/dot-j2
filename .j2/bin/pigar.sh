#!/usr/bash

# install pigar if not already installed
# pip install pigar 

# generate requirements.txt file
pigar -p requirements.txt -P . -o ">="
# -p : specify the output file name
# -P : specify the project directory
# -o : specify the version operator

