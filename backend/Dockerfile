FROM armhf/alpine:edge

ENV APP_ROOT=/app
ENV DJANGO_SETTINGS_MODULE=slurp.settings \
    GUNICORN_CONFIG=${APP_ROOT}/gunicorn-conf.py \
    PYTHONPATH=${APP_ROOT}:${PYTHONPATH} \
    PYTHONUNBUFFERED=true

# Build-only environment variables
ARG DJANGO_SECRET_KEY=build
ARG DJANGO_DATABASE_URL=sqlite:////

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

# Installs APK packages, makes Python 3 the default and updates pip and setuptools
COPY ./apk-packages.txt ${APP_ROOT}/
RUN apk add --no-cache $(grep -vE "^\s*#" ${APP_ROOT}/apk-packages.txt | tr "\n" " ") && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    pip3 install --no-cache-dir -U pip setuptools

COPY ./requirements.txt ${APP_ROOT}/
RUN pip3 install --no-cache-dir -r ${APP_ROOT}/requirements.txt

COPY . ${APP_ROOT}

# RUN django-admin collectstatic --no-input

ENTRYPOINT ["/app/bin/entrypoint"]
CMD ["/app/bin/run-django"]
EXPOSE 80
