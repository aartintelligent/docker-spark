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
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=password
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - /opt/postgres/data:/var/lib/postgresql/data
    ports:
      - '5432:5432'

  spark:
    build:
      context: .
    command: /opt/spark/sbin/start-master.sh
    depends_on:
      - database
    ports:
      - '7077:7077'
      - '8080:8080'

volumes:
  database-volume:
```