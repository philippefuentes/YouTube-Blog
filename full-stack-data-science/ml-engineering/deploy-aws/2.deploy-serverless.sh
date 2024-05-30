#!/bin/sh

cd "$(dirname "$0")" || exit

echo "Deploy yt-search-demo serverless"

sls deploy --aws-profile eussam-api-user