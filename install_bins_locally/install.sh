#!/usr/bin/bash

if [ "$#" -ne 1 ] ; then
  echo "Usage: $0 \${directory}"
  exit 1
fi

if [ ! -d "$1" ]; then
  echo "Failed to find the directory $1"
  exit 1
fi

cp -r $1/* .
