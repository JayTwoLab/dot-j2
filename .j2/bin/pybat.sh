#!/bin/bash

# Check if J2_ROOT is defined
if [ -z "$J2_ROOT" ]; then
    echo "[Error] J2_ROOT environment variable is not set."
    echo "Please run 'source env.bash' first."
    exit 1
fi

# Path to the core python script
PYBAT_CORE="$J2_ROOT/python/pybat.py"

# Check if the core script exists
if [ ! -f "$PYBAT_CORE" ]; then
    echo "[Error] pybat.py not found at: $PYBAT_CORE"
    exit 1
fi

# Execute the script with all passed arguments
python3 "$PYBAT_CORE" "$@"
