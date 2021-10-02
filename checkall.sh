#!/usr/bin/bash

cat modules.txt | while read ln; do
   git clone $ln tmp/$(basename $ln .git)
   ./check.py tmp/$(basename $ln .git)
done
