# Unxutils Separated scoop bucket

This is special scoop bucket generated from binaries from original unxutils manifest:

https://github.com/ScoopInstaller/Main/blob/69ac1b540540a3cf42724b7ffdc2b89c9a49445d/bucket/unxutils.json

`separate.py` python3 script takes `unxutils.json` from ScoopInstaller scoop bucket and creates entry in bucket/unxutils-XYZ.json
for each binary separatelly. For sha256 generation, valid unxutils folder has to exist for reference.

# Add to Scoop

```
scoop bucket add unxutils-separated https://github.com/alkuzad/unxutils-separated.git
```

Then install any package, prefixed by unxutils:

```
scoop install unxutils-grep
```

And use:

```batch
rem Note the lack of \ at the end, it's important
grep test "C:\Users\%USERNAME%.%USERDOMAIN%" -r
```

Or for ones that have same Windows command, use l-prefixed command:

```batch
lfind C:\Users -type d
```

# Linux prefix

Scoop will install original and aliased version with `l` prefix (from Linux). This way you can easily do `lsort` or `lfind` instead of mangling windows path.
