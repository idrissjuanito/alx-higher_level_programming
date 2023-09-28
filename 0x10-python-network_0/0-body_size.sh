#!/bin/bash
# Script extracts the content size from http request header
curl -sI $1 | grep Content-Length | cut -d ' ' -f2
