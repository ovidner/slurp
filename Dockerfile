FROM armhf/alpine:3.5

ENV APP_ROOT=/app \
    DJANGO_SETTINGS_MODULE=slurp.settings \
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

RUN django-admin collectstatic --no-input

ENTRYPOINT ["/app/bin/entrypoint"]
CMD ["/app/bin/django"]
EXPOSE 80
