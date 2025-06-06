FROM node:20-alpine AS y-provider-builder

WORKDIR /home/frontend/

COPY ./src/frontend/package.json ./package.json
COPY ./src/frontend/yarn.lock ./yarn.lock
COPY ./src/frontend/servers/y-provider/package.json ./servers/y-provider/package.json
COPY ./src/frontend/packages/eslint-config-impress/package.json ./packages/eslint-config-impress/package.json

RUN yarn install

COPY ./src/frontend/packages/eslint-config-impress ./packages/eslint-config-impress
COPY ./src/frontend/servers/y-provider ./servers/y-provider

WORKDIR /home/frontend/servers/y-provider
RUN yarn build

FROM node:20-alpine AS y-provider

WORKDIR /home/frontend/

COPY ./src/frontend/package.json ./package.json
COPY ./src/frontend/yarn.lock ./yarn.lock
COPY ./src/frontend/servers/y-provider/package.json ./servers/y-provider/package.json

WORKDIR /home/frontend/servers/y-provider

COPY --from=y-provider-builder \
    /home/frontend/servers/y-provider/dist \
    ./dist

RUN NODE_ENV=production yarn install --frozen-lockfile

# Un-privileged user running the application
ARG DOCKER_USER
USER ${DOCKER_USER}

# Copy entrypoint
COPY ./docker/files/usr/local/bin/entrypoint /usr/local/bin/entrypoint
ENTRYPOINT [ "/usr/local/bin/entrypoint" ]

CMD ["yarn", "start"]
