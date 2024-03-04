#!/bin/bash
# Displays the status code
curl -s -o /dev/null -w "%{response_code}" "$1"
