#!/bin/bash
# sends curl request with json
curl -s --json @$2 -H "Content-Type: Application/json" $1
