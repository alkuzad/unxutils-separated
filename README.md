This is content of https://github.com/ScoopInstaller/Main/blob/69ac1b540540a3cf42724b7ffdc2b89c9a49445d/bucket/unxutils.json 
separated to individual packages.


# Add to Scoop

```
scoop bucket add unxutils-separated https://github.com/alkuzad/unxutils-separated.git
```

Then install any package, prefixed by unxutils:

```
scoop install unxutils-grep
```

# Linux prefix

Scoop will install original and aliased version with `l` prefix (from Linux). This way you can easily do `lsort` or `lfind` instead of mangling windows path.
