#!/bin/bash
#A script that prints the body of a response message
curl -I $1 | awk 'BEGIN { RS = "" } { print $0 }' | tail -n 1
