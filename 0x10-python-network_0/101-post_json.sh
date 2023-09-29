#!/bin/bash
# Docs
curl -s -d @"$2" -H "Content-Type: application/json" "$1" -X POST
