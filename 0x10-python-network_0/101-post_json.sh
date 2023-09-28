#!/bin/bash
# sends curl request with json
curl -s --data -H "Content-Type: application/json" -H "Accept: application/json" @$2 $1 -X POST
