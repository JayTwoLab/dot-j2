# Ksh environment setup
# Add your environment variables and settings here
# env.ksh - Ksh version
# Set current /.j2 directory
export J2_ROOT="$PWD"

if [[ ! -d "$J2_ROOT" ]]; then
	echo "[Warning] .j2 directory not found in the current path."
fi

export PATH="$J2_ROOT/bin:$PATH"
export LD_LIBRARY_PATH="$J2_ROOT/lib:$LD_LIBRARY_PATH"

echo "J2 Environment Activated."
echo "J2_ROOT is set to: $J2_ROOT"
