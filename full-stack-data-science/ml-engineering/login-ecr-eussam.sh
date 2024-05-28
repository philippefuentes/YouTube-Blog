#!/bin/bash

# aws cli v2
aws_account='294263178210'
aws_region='us-east-1'

password=$(aws ecr get-login-password --profile eussam-api-user --region $aws_region)
echo $password | docker login --username AWS --password-stdin $aws_account.dkr.ecr.$aws_region.amazonaws.com
