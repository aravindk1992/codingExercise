#!/usr/bin/env bash

echo "Commiting to Github"
git add .
git commit -m "$1"
git push -u origin master