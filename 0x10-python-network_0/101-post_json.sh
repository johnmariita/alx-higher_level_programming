#!/bin/bash
# A script that sends a JSON POST request to a URL and displays the body of the response.
curl -s -H "Content-Type: application/json" "$1" -d @$2
