#!/usr/bin/env fish 

set -x TERM xterm-256color

set -x J2_ROOT (pwd)

if not test -d $J2_ROOT
    echo "[Warning] .j2 directory not found in the current path."
end

set -x PATH $J2_ROOT/bin $PATH
set -x LD_LIBRARY_PATH $J2_ROOT/lib $LD_LIBRARY_PATH

echo "J2 Environment Activated."
echo "J2_ROOT is set to: $J2_ROOT"

