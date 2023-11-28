param(
    [string] $BuildArtifactsPath,
    [switch] $UseTypeSpecNext
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
    $buildArtifactsPathArg = $BuildArtifactsPath ? "--build-artifacts-path=`"$BuildArtifactsPath`"" : ""
    invoke "python --version"
    invoke "python eng/scripts/initialize.py --use-typespec-next=$UseTypeSpecNext $buildArtifactsPathArg"

    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
