#!/bin/bash
# queries with curl and print status code
curl -sw "%{response_code}" $1 -o /dev/null
