FROM mcr.microsoft.com/devcontainers/javascript-node:20

# Install Python 3.12 and pip
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get -y install --no-install-recommends python3.12 python3.12-venv python3.12-dev python3-pip \
    && python3.12 -m pip install --upgrade pip \
    && ln -sf /usr/bin/python3.12 /usr/local/bin/python \
    && ln -sf /usr/bin/python3.12 /usr/local/bin/python3 \
    && ln -sf /usr/bin/pip3 /usr/local/bin/pip

# Install pnpm globally
RUN npm install -g pnpm

# Install autorest globally
RUN npm install -g autorest
