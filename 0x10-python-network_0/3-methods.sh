#!/bin/bash
#A script that prints the allowed methods
curl -sI $1 | grep Allow | cut -d " " -f 2-
