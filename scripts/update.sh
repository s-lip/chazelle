#!/bin/bash
set -ev
umask 0002
DATE=`date '+%Y-%m%d-%H%M'`
git fetch origin master
git add -A
git commit -m "Auto-commit $DATE" && (
        mergebase=$(git merge-base FETCH_HEAD master)
        git merge-tree $mergebase master FETCH_HEAD | grep -qv 'changed in both'
        git rebase FETCH_HEAD
        git push origin master
) || (
        echo skipping commit
        git merge origin/master
)
