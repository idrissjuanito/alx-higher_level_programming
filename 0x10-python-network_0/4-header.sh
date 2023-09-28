#!/bin/bash
# sends a get request with header values
curl -H "X-School-User-Id=80" $1 -X GET
