docker build -t example1 .
```output
[+] Building 1.2s (7/7) FINISHED                                                
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 134B                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.9              0.4s
 => [1/3] FROM docker.io/library/python:3.9@sha256:603ac689b89c2a59791a4e  0.0s
 => CACHED [2/3] RUN apt-get upgrade -y && apt-get update -y               0.0s
 => [3/3] RUN python -c 'print("Hello World")'                             0.4s
 => exporting to image                                                     0.2s
 => => exporting layers                                                    0.2s
 => => writing image sha256:1d2804700ef5a526418f8e89cdf029af2a572476bd089  0.0s
 => => naming to docker.io/library/example1  

```


