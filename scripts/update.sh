#!/bin/bash
set -ev
umask 0002
DATE=`date '+%Y-%m%d-%H%M'`
git fetch origin master
git add -A
git commit -m "Auto-commit $DATE" || (echo skipping commit; exit 0)
echo mergebase=$(git merge-base FETCH_HEAD master)
mergebase=$(git merge-base FETCH_HEAD master)
echo git merge-tree $mergebase master FETCH_HEAD | grep -qv 'changed in both'
git merge-tree $mergebase master FETCH_HEAD | grep -qv 'changed in both'
echo git rebase FETCH_HEAD
git rebase FETCH_HEAD
echo git push origin master
git push origin master
