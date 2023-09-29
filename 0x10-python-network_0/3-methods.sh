#!/bin/bash
# Docs 
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
