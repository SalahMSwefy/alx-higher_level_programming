#!/usr/bin/bash
# This script will print the size of the body of the response

curl -si "$1" | grep "Content-Length" | cut -d " " -f 2
