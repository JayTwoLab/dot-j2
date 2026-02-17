#!/bin/csh -f

setenv TERM xterm-256color

setenv J2_ROOT $PWD

if (! -d $J2_ROOT) then
	echo "[Warning] .j2 directory not found in the current path."
endif

setenv PATH "$J2_ROOT/bin:$PATH"
setenv LD_LIBRARY_PATH "$J2_ROOT/lib:$LD_LIBRARY_PATH"

echo "J2 Environment Activated."
echo "J2_ROOT is set to: $J2_ROOT"


