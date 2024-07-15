#!/bin/bash
echo Getting file list...
find $1 -exec file {} \; | grep -i elf\ > binaries.txt
python bins.py
