#!/bin/bash
#A script that prints the allowed methods
curl -I $1 | grep Allow | cut -d: -f2 | tr -d " "
