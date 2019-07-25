
###############################################
# LEGACY
# Instead: have bunch of configuration files sitting in a well-known spot, discover them, feed them to AutoRest, done.

regenExpected = (opts,done) ->
  outputDir = if !!opts.outputBaseDir then "#{opts.outputBaseDir}/#{opts.outputDir}" else opts.outputDir
  keys = Object.getOwnPropertyNames(opts.mappings)
  instances = keys.length

  for kkey in keys
    optsMappingsValue = opts.mappings[kkey]
    key = kkey.trim();

    swaggerFiles = (if optsMappingsValue instanceof Array then optsMappingsValue[0] else optsMappingsValue).split(";")
    args = [
      "--#{opts.language}",
      "--clear-output-folder",
      "--output-folder=#{outputDir}/#{key}",
      "--license-header=#{if !!opts.header then opts.header else 'MICROSOFT_MIT_NO_VERSION'}",
      "--enable-xml",
      "--basic-setup-py",
      "--trace",
    ]

    for swaggerFile in swaggerFiles
      args.push("--input-file=#{if !!opts.inputBaseDir then "#{opts.inputBaseDir}/#{swaggerFile}" else swaggerFile}")

    if (opts.addCredentials)
      args.push("--#{opts.language}.add-credentials=true")

    if (opts.vanilla)
      args.push("--#{opts.language}.vanilla=true")

    if (opts.azureArm)
      args.push("--#{opts.language}.azure-arm=true")

    if (opts.flatteningThreshold)
      args.push("--#{opts.language}.payload-flattening-threshold=#{opts.flatteningThreshold}")

    if (opts.keepVersion)
      args.push("--#{opts.language}.keep-version-file=true")

    if (!!opts.nsPrefix)
      if (optsMappingsValue instanceof Array && optsMappingsValue[1] != undefined)
        args.push("--#{opts.language}.namespace=#{optsMappingsValue[1]}")
      else
        args.push("--#{opts.language}.namespace=#{[opts.nsPrefix, key.replace(/\/|\./, '')].join('.')}")

    if (opts['override-info.version'])
      args.push("--override-info.version=#{opts['override-info.version']}")
    if (opts['override-info.title'])
      args.push("--override-info.title=#{opts['override-info.title']}")
    if (opts['override-info.description'])
      args.push("--override-info.description=#{opts['override-info.description']}")

    autorest args,() =>
      instances--
      return done() if instances is 0

defaultMappings = {
  'AcceptanceTests/AdditionalProperties': 'additionalProperties.json',
  'AcceptanceTests/ParameterFlattening': 'parameter-flattening.json',
  'AcceptanceTests/BodyArray': 'body-array.json',
  'AcceptanceTests/BodyBoolean': 'body-boolean.json',
  'AcceptanceTests/BodyByte': 'body-byte.json',
  'AcceptanceTests/BodyComplex': 'body-complex.json',
  'AcceptanceTests/BodyDate': 'body-date.json',
  'AcceptanceTests/BodyDateTime': 'body-datetime.json',
  'AcceptanceTests/BodyDateTimeRfc1123': 'body-datetime-rfc1123.json',
  'AcceptanceTests/BodyDuration': 'body-duration.json',
  'AcceptanceTests/BodyDictionary': 'body-dictionary.json',
  'AcceptanceTests/BodyFile': 'body-file.json',
  'AcceptanceTests/BodyFormData': 'body-formdata.json',
  'AcceptanceTests/BodyInteger': 'body-integer.json',
  'AcceptanceTests/BodyNumber': 'body-number.json',
  'AcceptanceTests/BodyString': 'body-string.json',
  'AcceptanceTests/ExtensibleEnums': 'extensible-enums-swagger.json',
  'AcceptanceTests/Header': 'header.json',
  'AcceptanceTests/Http': 'httpInfrastructure.json',
  'AcceptanceTests/Report': 'report.json',
  'AcceptanceTests/RequiredOptional': 'required-optional.json',
  'AcceptanceTests/Url': 'url.json',
  'AcceptanceTests/Validation': 'validation.json',
  'AcceptanceTests/CustomBaseUri': 'custom-baseUrl.json',
  'AcceptanceTests/CustomBaseUriMoreOptions': 'custom-baseUrl-more-options.json',
  'AcceptanceTests/ModelFlattening': 'model-flattening.json',
  'AcceptanceTests/Xml': 'xml-service.json',
  'AcceptanceTests/UrlMultiCollectionFormat' : 'url-multi-collectionFormat.json'
}

defaultAzureMappings = {
  'AcceptanceTests/AzureBodyDuration': 'body-duration.json',
  'AcceptanceTests/AzureReport': 'azure-report.json',
  'AcceptanceTests/AzureParameterGrouping': 'azure-parameter-grouping.json',
  'AcceptanceTests/ModelFlattening': 'model-flattening.json',
  'AcceptanceTests/CustomBaseUri': 'custom-baseUrl.json'
}

# The list is mostly built on Swaggers that uses CloudError feature
# These Swagger should be modified to test their features, and not the CloudError one
defaultARMMappings = {
  'AcceptanceTests/Head': 'head.json',
  'AcceptanceTests/HeadExceptions': 'head-exceptions.json',
  'AcceptanceTests/StorageManagementClient': 'storage.json',
  'AcceptanceTests/Lro': 'lro.json',
  'AcceptanceTests/SubscriptionIdApiVersion': 'subscriptionId-apiVersion.json',
  'AcceptanceTests/Paging': 'paging.json',
  'AcceptanceTests/AzureSpecials': 'azure-special-properties.json',
}

swaggerDir = "node_modules/@microsoft.azure/autorest.testserver/swagger"

task 'regenerate-python', '', (done) ->
  regenExpected {
    'outputBaseDir': 'test/vanilla',
    'inputBaseDir': swaggerDir,
    'mappings': defaultMappings,
    'outputDir': 'Expected',
    'language': 'python',
    'flatteningThreshold': '1',
    'vanilla': true,
    'keepVersion': true
  },done
  return null

task 'regenerate-pythonazure', '', (done) ->
  regenExpected {
    'outputBaseDir': 'test/azure',
    'inputBaseDir': swaggerDir,
    'mappings': defaultAzureMappings,
    'outputDir': 'Expected',
    'language': 'python',
    'flatteningThreshold': '1'
  },done
  return null

task 'regenerate-pythonarm', '', (done) ->
  regenExpected {
    'outputBaseDir': 'test/azure',
    'inputBaseDir': swaggerDir,
    'mappings': defaultARMMappings,
    'outputDir': 'Expected',
    'language': 'python',
    'azureArm': true,
    'flatteningThreshold': '1'
  },done
  return null

task 'regenerate', "regenerate expected code for tests", ['regenerate-python', 'regenerate-pythonazure', 'regenerate-pythonarm'], (done) ->
  done();
