#!/bin/bash
# sends a post request with curl along some data
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" $1 -X POST
