#!/bin/bash
# displays all accepted http methods
curl -sw "%header{Allow}" $1
