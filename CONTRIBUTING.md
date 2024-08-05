# Contributing

## @azure-tools/typespec-python

### Regenerating

`npm run regenerate`

#### Flags

If you're adding flags, you'll need to add a `--` before including the flags

| Flag | Description |
|------|-------------|
| `--name` | Name of the file you want to generate. Will only generate files that include `--name` |
| `--flavor=azure\|unbranded` | Regenerate either azure or unbranded flavor |
| `--debug` | If you want to debug through the code |

**Example**
`npm run regenerate -- --name api --flavor unbranded`

## @autorest/python

### Regenerating
