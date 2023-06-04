docker build --progress=plain --no-cache -t example3 .

```output
#1 [internal] load .dockerignore
#1 transferring context: 2B done
#1 DONE 0.0s

#2 [internal] load build definition from Dockerfile
#2 transferring dockerfile: 134B done
#2 DONE 0.0s

#3 [internal] load metadata for docker.io/library/python:3.9
#3 DONE 0.9s

#4 [1/3] FROM docker.io/library/python:3.9@sha256:603ac689b89c2a59791a4e7cd3d727f2a673ac3df02dabbd97b0d85bb1eca4e7
#4 DONE 0.0s

#5 [2/3] RUN apt-get upgrade -y && apt-get update -y
#5 CACHED

#6 [3/3] RUN python -c 'print("Hello World")'
#6 CACHED

#7 exporting to image
#7 exporting layers done
#7 writing image sha256:1d2804700ef5a526418f8e89cdf029af2a572476bd0899163187e9ccbb570ad7 done
#7 naming to docker.io/library/example2 done
#7 DONE 0.0s

```
