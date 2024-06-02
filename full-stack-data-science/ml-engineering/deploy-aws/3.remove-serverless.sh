#!/bin/sh

cd "$(dirname "$0")" || exit

echo "Remove yt-search-demo serverless"

sls remove --aws-profile eussam-api-user