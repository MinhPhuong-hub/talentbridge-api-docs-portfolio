#!/usr/bin/env bash

set -euo pipefail

curl -X POST \
  http://127.0.0.1:4010/jobs \
  -H "Authorization: Bearer demo-token" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Backend Developer",
    "description": "Build and maintain recruitment platform APIs.",
    "location": "Ho Chi Minh City"
  }'
