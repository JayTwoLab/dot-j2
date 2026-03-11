#!/bin/bash

# Check if J2_ROOT is defined
if [ -z "$J2_ROOT" ]; then
    echo "[Error] J2_ROOT environment variable is not set."
    echo "Please run 'source env.bash' first."
    exit 1
fi

# Path to the core python script
PROCESS_MONITOR="$J2_ROOT/python/process_monitor.py"

# Check if the core script exists
if [ ! -f "$PROCESS_MONITOR" ]; then
    echo "[Error] process_monitor.py not found at: $PROCESS_MONITOR"
    exit 1
fi

# Execute the script with all passed arguments
python3 "$PROCESS_MONITOR" "$@"
