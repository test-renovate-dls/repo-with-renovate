# Run in a container

Pre-built containers with repo-with-renovate and its dependencies already
installed are available on [Github Container Registry](https://ghcr.io/test-renovate-dls/repo-with-renovate).

## Starting the container

To pull the container from github container registry and run:

```
$ docker run ghcr.io/test-renovate-dls/repo-with-renovate:latest --version
```

To get a released version, use a numbered release instead of `latest`.
