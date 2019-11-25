FROM node:12.13.1

LABEL maintainer="9ian1i <9ian1itp@gmail.com>"

COPY . /app/

WORKDIR /app

RUN npm install --registry=https://registry.npm.taobao.org --cache=$HOME/.npm/.cache/cnpm --disturl=https://npm.taobao.org/dist --userconfig=$HOME/.cnpmrc

RUN npm run build


FROM nginx

LABEL maintainer="9ian1i <9ian1itp@gmail.com>"

COPY --from=0 /app/dist /usr/share/nginx/html
