#!/bin/bash
# Docs
curl -w "%{http_code}" "$1" -so /dev/null
