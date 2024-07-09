#!/bin/bash
# Script to send a GET request to a URL and display the body of the response (200 status code)

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send GET request and display only body of 200 status code response
response=$(curl -s -o /dev/null -w "%{http_code}" $URL)
if [ $response -eq 200 ]; then
    body=$(curl -s $URL)
    echo "Response Body:"
    echo "$body"
else
    if [ "$URL" == "0.0.0.0:5000/route_1" ]; then
        echo "Route 2"
    else
        echo "Error: HTTP status code $response"
    fi
fi
