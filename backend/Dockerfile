FROM node:22-alpine AS frontend-build
WORKDIR /frontend
COPY frontend/package.json ./
RUN npm install --no-audit --no-fund
COPY frontend/ ./
ENV VITE_API_URL=""
# Build for modern browsers without changing the supplied frontend config.
RUN node --input-type=module -e "import { build } from 'vite'; import vue from '@vitejs/plugin-vue2'; await build({ configFile: false, plugins: [vue()], build: { target: 'es2020' } });"

FROM python:3.13-slim
LABEL maintainer="danylo.t@mate.academy"

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY backend/ /app/
COPY --from=frontend-build /frontend/dist /frontend-dist
ENV FRONTEND_DIST=/frontend-dist

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
