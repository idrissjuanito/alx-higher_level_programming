#!/bin/bash
# displays all accepted http methods
curl -sI $1 -X OPTIONS | grep 'Allow:' | cut -d ' ' -f2-
