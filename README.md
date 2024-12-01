Docker Spark
=============

### Usage Docker

```shell
docker build . -t aartintelligent/spark:latest
```

```shell
docker push aartintelligent/spark:latest
```

### Usage Docker Compose

```shell
docker compose build
```

```shell
docker compose up -d
```

```shell
docker compose run -it spark bin/spark-submit app/example.py
```

```shell
docker compose down -v
```

### Compose

```yaml
services:

  database:
    image: postgres:17
    user: root
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=spark
      - POSTGRES_PASSWORD=password
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - database-volume:/var/lib/postgresql/data
      # - /opt/postgres/data:/var/lib/postgresql/data
    ports:
      - '5432:5432'

  spark:
    build:
      context: .
    command: bin/spark-shell
    volumes:
      - ./app:/opt/spark/app
    ports:
      - '7077:7077'
      - '8080:8080'

volumes:
  database-volume:
```