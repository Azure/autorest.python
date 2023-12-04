#Requires -Version 7.0

param(
    [Parameter()]
    [ValidateSet("autorest", "typespec")]
    [string] $Package,
    
    [switch] $CheckCode,
    [switch] $Regenerate,
    [switch] $CheckChanges
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 3.0

$root = (Resolve-Path "$PSScriptRoot/../..").Path.Replace('\', '/')

function invoke($command) {
    Write-Host "> $command"
    Invoke-Expression $command
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Command failed: $command"
        exit $LASTEXITCODE
    }
}

Push-Location $root
try {
    $packageArg = $Package ? "--package=$Package" : ""

    invoke "python -u eng/scripts/test.py $packageArg --check-code=$CheckCode --regenerate=$Regenerate --check-change=$CheckChanges"

    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
