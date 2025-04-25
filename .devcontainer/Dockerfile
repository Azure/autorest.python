FROM mcr.microsoft.com/devcontainers/javascript-node:20

RUN corepack enable pnpm \
  && echo 'alias pnpm="corepack pnpm"' >> /home/node/.bash_aliases

# Install Python 3.12 and pip
RUN set -ex && \
    apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends wget build-essential libreadline-dev \
    libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev \
    libbz2-dev libffi-dev zlib1g-dev && \
    cd /tmp && \
    wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz && \
    tar -xf Python-3.12.2.tgz && \
    cd Python-3.12.2 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    ln -sf /usr/local/bin/python3.12 /usr/local/bin/python && \
    ln -sf /usr/local/bin/python3.12 /usr/local/bin/python3 && \
    ln -sf /usr/local/bin/pip3.12 /usr/local/bin/pip && \
    cd / && \
    rm -rf /tmp/Python-3.12.2 /tmp/Python-3.12.2.tgz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*