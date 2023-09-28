#!/bin/bash
# Script to display content if request successfull
respons=$(curl -o /tmp/reqout -sw 'Code: %{response_code}' $1);
code=$(echo $respons | grep 'Code' | cut -d ' ' -f2);
if [[ $code == "200" ]]; then
    cat /tmp/reqout
fi
