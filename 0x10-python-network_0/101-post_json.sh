#!/bin/bash
# sends curl request with json
curl -s --json @$2 $1 -X POST
