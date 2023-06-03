# titanic-docker

Download data:
```shell
mkdir -p data
curl -L https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv -o data/titanic.csv

```

Build app:
```shell
docker build -t titanic-app-predict:latest --target api .
```

Run app:
```shell
docker run -p 5000:5000 --mount type=bind,src=${PWD}/data,dst=/app/data titanic-app-predict:latest 
```

manual prediction:
```shell
curl -X POST -H 'Content-Type: application/json' --data '{"Pclass": 2, "Sex": "male", "Age": 22, "SibSp" :1, "Parch": 0, "Fare":7.2, "Embarked":"S"}' http://localhost:5000/predict
```



everything via compose:
```shell
docker compose up --build
```