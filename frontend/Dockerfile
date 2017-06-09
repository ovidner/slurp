FROM armhf/alpine:edge

ENV APP_ROOT=/app

RUN mkdir -p ${APP_ROOT}/build
WORKDIR ${APP_ROOT}

# Installs APK packages and prepends "daemon off;" to make sure nginx does not daemonize.
COPY ./apk-packages.txt ${APP_ROOT}/apk-packages.txt
RUN apk add --no-cache $(grep -vE "^\s*#" ${APP_ROOT}/apk-packages.txt | tr "\n" " ") && \
  cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig && \
  echo "daemon off;" > /etc/nginx/nginx.conf && \
  cat /etc/nginx/nginx.conf.orig >> /etc/nginx/nginx.conf

# Installs NPM packages with Yarn
COPY ./package.json ./yarn.lock ${APP_ROOT}/
RUN yarn install && \
    yarn cache clean

COPY . ${APP_ROOT}
RUN ln -sf ${APP_ROOT}/etc/nginx/conf.d /etc/nginx/conf.d

ENTRYPOINT ["/app/bin/entrypoint"]
CMD ["nginx"]
