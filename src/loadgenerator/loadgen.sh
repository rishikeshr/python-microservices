#!/bin/bash
locust -f locust.py --headless --host="http://${FRONTEND_ADDR}" -u "${USERS:-10}" -r "${SPAWN_RATE:-20}" -t "${RUN_TIME:-1h30m}" 2>&1