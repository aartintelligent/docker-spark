FROM spark:python3

USER root

COPY requirements.txt /requirements.txt

RUN if [ -s "/requirements.txt" ]; then \
        if ! pip install -r "/requirements.txt"; then \
            echo "Failed to install requirements from requirements.txt"; \
            exit 1; \
        fi; \
    fi

COPY --chown=spark:spark app /opt/spark/app

WORKDIR /opt/spark

USER spark
