# titanic-docker

Build Train:
```shell
docker build -t titanic-docker-train:latest --target train .
```

Execute Train:
```shell
docker run -it titanic-docker-train:latest
```


Serve prediction:
```shell
docker run -d titanic-app-predict:latest
```

Frontend:
```shell
docker run -d titanic-app-frontend:latest
```

everything via compose:
```shell
docker compose up
```