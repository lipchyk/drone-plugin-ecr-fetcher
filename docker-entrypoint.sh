#!/bin/sh
set -e

aws_region=${PLUGIN_AWS_REGION:-eu-central-1}

$(aws ecr get-login --no-include-email --region ${aws_region})
exec ./pull_images.py
