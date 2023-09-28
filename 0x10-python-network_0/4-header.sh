#!/bin/bash
# sends a get request with header values
curl -sH "X-School-User-Id:80" $1 -X GET
