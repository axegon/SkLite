#!/bin/bash

for pyfile in $(find ${BASH_SOURCE%/*}/../sklite -iname "*.py")
do
    echo "Checking $pyfile ..."
    pylint $pyfile
done

cd ${BASH_SOURCE%/*}/../sklite
flake8
