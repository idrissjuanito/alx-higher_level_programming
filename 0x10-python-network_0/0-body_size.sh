#!/bin/bash
# Script extracts the content size from http request header
if [[ ! $# -eq 1 ]]; then
    echo "USAGE: command URL";
    exit 1;
fi
curl -sI $1 | grep Content-Length | cut -d ' ' -f2
