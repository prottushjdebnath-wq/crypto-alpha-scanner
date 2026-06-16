#!/bin/bash

source /opt/trading-bot/venv/bin/activate

while true
do
    echo "=================================="
    echo "SCAN STARTED $(date)"
    echo "=================================="

    python run_scanner.py

    echo "Sleeping 300 seconds..."
    sleep 300
done
