#!/bin/bash
# Script to display content if request successfull
[[ $(curl -sw "%{response_code}" $1 -o /tmp/reqout) == '200' ]] && cat /tmp/reqout
