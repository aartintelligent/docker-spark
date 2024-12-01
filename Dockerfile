FROM maven:eclipse-temurin AS builder

COPY pom.xml /pom.xml

RUN mvn dependency:copy-dependencies -DoutputDirectory=/jars -B

FROM spark:python3

USER root

COPY --chown=spark:spark app /opt/spark/app

COPY --from=builder --chown=spark:spark /jars/* /opt/spark/jars/

COPY requirements.txt /requirements.txt

RUN if [ -s "/requirements.txt" ]; then \
        if ! pip install -r "/requirements.txt"; then \
            echo "Failed to install requirements from requirements.txt"; \
            exit 1; \
        fi; \
    fi

WORKDIR /opt/spark

USER spark
