#!/bin/bash
# script to send custom header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
