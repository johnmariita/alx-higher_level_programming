#A script that gets the Content-Length of a domain

curl -I $1 | grep Content-Length | cut -d: -f2 | tr -d " "
