#!/bin/sh

cd "$(dirname "$0")" || exit

echo "Validate yt-search-demo serverless"

# docker run --rm \
#     -v "$(pwd)":/root/serverless \
#     -v ~/.aws:/root/.aws \
#     -w /root/serverless \
#     softinstigate/serverless \
#     package --aws-profile vetup-prod-user-terraform --stage prod

# docker run --rm \
#     -v "$(pwd)":/root/serverless \
#     -v ~/.aws:/root/.aws \
#     -w /root/serverless \
#     serverless-cli \
#     package --aws-profile eussam-api-user

sls package --aws-profile eussam-api-user