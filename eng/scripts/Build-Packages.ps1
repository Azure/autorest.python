param(
    [string] $BuildNumber,
    [string] $Output,
    [switch] $Prerelease,
    [switch] $PublishInternal
)

$ErrorActionPreference = 'Stop'

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
    $versionArg = $Prerelease ? "--version-suffix=-alpha.$BuildNumber" : ""
    $internalArg = $PublishInternal ? "--publish-internal" : ""

    invoke "python -u eng/scripts/build.py --output-dir=`"$Output`" $versionArg $internalArg"

    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
