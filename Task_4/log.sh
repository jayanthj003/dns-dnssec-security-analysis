#!/bin/bash
LOG_FILE="docker_cpu_log.csv"
echo "Timestamp,Container,CPU%" > "$LOG_FILE"
while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    docker stats --no-stream --format "{{.Name}},{{.CPUPerc}}" | while read line; do
        echo "$TIMESTAMP,$line" >> "$LOG_FILE"
    done
    sleep 1
done

