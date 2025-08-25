FROM mcr.microsoft.com/devcontainers/base:debian

WORKDIR /computation

COPY . .

RUN apt-get update

# Aspell
RUN apt-get install aspell -y

# Python
RUN apt-get install python3 -y && \
    apt-get install python3-pip -y && \
    apt-get install pipenv  -y && \
    ln -s /usr/bin/python3.11 /usr/bin/python

# Haskell
RUN apt-get install ghc -y

# Java
RUN apt install default-jre  -y
RUN apt install default-jdk -y

RUN pipenv sync --system -d

RUN adduser -u 5678 --disabled-password --gecos "" computation && chown -R computation /computation
USER computation