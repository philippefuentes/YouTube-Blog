#!/bin/sh

cd "$(dirname "$0")" || exit

echo "Force deploy yt-search-demo serverless"

sls deploy --force --aws-profile eussam-api-user