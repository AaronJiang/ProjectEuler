#! /bin/bash
#ex: ./run.sh problem001.c

filename=$1
rm a.out
gcc euler.c $filename -lm
./a.out