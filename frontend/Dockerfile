ARG NODE_VERSION=18.17.0

FROM node:18.17.0-slim as base

ARG PORT=3000

WORKDIR /src

# Build
FROM base as build

COPY --link package.json yarn.lock .yarnrc.yml ./

RUN yarn install

COPY --link . .

RUN yarn build

# Run
FROM base

ENV PORT=8080

COPY --from=build /src/.output /src/.output
# Optional, only needed if you rely on unbundled dependencies
COPY --from=build /src/node_modules /src/node_modules

CMD [ "node", ".output/server/index.mjs" ]
