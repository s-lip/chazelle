#!/bin/bash
set -e
echo umask 0002
umask 0002
DATE=`date '+%Y-%m%d-%H%M'`
echo DATE=$DATE
echo git add -A
git add -A
echo git commit -m "Auto-commit $DATE"
git commit -m "Auto-commit $DATE"
echo git fetch origin master
git fetch origin master
echo mergebase=$(git merge-base FETCH_HEAD master)
mergebase=$(git merge-base FETCH_HEAD master)
echo git merge-tree $mergebase master FETCH_HEAD | grep -qv 'changed in both'
git merge-tree $mergebase master FETCH_HEAD | grep -qv 'changed in both'
echo git rebase FETCH_HEAD
git rebase FETCH_HEAD
echo git push origin master
git push origin master
