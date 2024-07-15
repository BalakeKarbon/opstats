#!/bin/bash
objdump -d $1 | sed  '/[^\t]*\t[^\t]*\t/!d' | cut -f 3 | sed 's/ .*$//' > opcodes.txt
python getOpStats.py
