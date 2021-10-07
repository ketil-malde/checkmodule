#!/usr/bin/bash

cat modules.txt | while read ln; do
   mname=$(echo $ln | awk '{print $NF}')
   git clone $ln tmp/$(basename $mname .git)
   ./check.py tmp/$(basename $mname .git)
done
