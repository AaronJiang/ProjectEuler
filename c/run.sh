#! /bin/bash
#eg ./run.sh problem001.c

filename=$1
[ -f "./a.out" ] && rm a.out
gcc euler.c $filename -lm
[ -f "./a.out" ] && ./a.out
