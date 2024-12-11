#!/bin/bash

dois='10.1111/bjet.13089 10.1007/s10758-022-09613-x 10.54941/ahfe1003158'

for doi in dois; do
    /home/thiago/repos/notebooks/venv/bin/python3 -m PyPaperBot --doi="$doi" --dwn-dir="/home/thiago/systematic_review" -use-doi-as-filename
done

