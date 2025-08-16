FROM mcr.microsoft.com/devcontainers/python:3.13

WORKDIR /computation

COPY . .

RUN apt-get update

RUN apt-get install aspell -y

RUN apt-get install ghc -y

RUN apt-get install ruby-full

RUN pipenv sync --system -d

RUN adduser -u 5678 --disabled-password --gecos "" computation && chown -R computation /computation
USER computation