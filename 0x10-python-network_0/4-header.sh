#!/bin/bash
# This script will take in a URL, send a GET request to the URL, and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
