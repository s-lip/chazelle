#!/bin/bash
set -e
git fetch origin master
mergebase=$(git merge-base FETCH_HEAD master)
echo $mergebase
git merge-tree $mergebase master FETCH_HEAD | grep -qv 'changed in both'
git rebase FETCH_HEAD
