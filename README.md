# README

## Build and deploy

Build

```sh
cd robotics_software_interaction
jupyter-book build --all .
```

Then commit and push your changes

```sh
git commit -a -m "Blabla"
git push
```

Deploy with:

```sh
ghp-import -n -p -f _build/html
```
