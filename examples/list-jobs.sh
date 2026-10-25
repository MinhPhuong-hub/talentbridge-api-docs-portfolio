#!/usr/bin/env bash

set -euo pipefail

curl \
  -H "Prefer: example=normal" \
  http://127.0.0.1:4010/jobs
