#!/bin/bash
# Displays all HTTP methods the server will accept, and takes a URL
curl -sI "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
