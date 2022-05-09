FROM debian

RUN \
    apt-get update && \
    apt-get install -y openssh-server wget make && \
    mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config && \
    echo 'root:change_me' | chpasswd && \
    useradd -m arikoi -s /bin/bash && \
    echo 'arikoi:change_me_too' | chpasswd

COPY ./requirements /root/requirements
RUN xargs apt-get install -y < /root/requirements

RUN apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
