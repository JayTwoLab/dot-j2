
# current .j2 directory
$J2_ROOT = Get-Location
$env:J2_ROOT = $J2_ROOT

if (-not (Test-Path $J2_ROOT)) {
	Write-Host "[Warning] .j2 folder not found in the current directory."
}

$env:PATH = "$J2_ROOT/bin;$J2_ROOT/lib;$env:PATH"

Write-Host "J2 Environment Activated."
Write-Host "J2_ROOT is set to: $J2_ROOT"
