#!/bin/bash
# sends curl request with json
curl -s --data @$2 -H "Content-Type: application/json" -H "Accept: application/json" $1 -X POST
