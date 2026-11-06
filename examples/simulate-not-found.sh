#!/usr/bin/env bash
set -euo pipefail

curl -i -H "Prefer: code=404" http://127.0.0.1:4010/jobs/job_unknown
