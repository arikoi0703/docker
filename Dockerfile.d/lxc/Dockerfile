From debian

RUN apt-get update && \
    apt-get install -y lxc

RUN echo 'root:WhatASecurityPassword' | chpasswd
RUN useradd -g lxd -s /bin/bash -m peto
RUN echo 'peto:1204' | chpasswd

CMD ["tail", "-f", "/dev/null"]
