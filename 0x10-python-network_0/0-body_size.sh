#!/bin/bash
# Docs 
curl -w "%{size_download}\n" "$1" -so /dev/null
