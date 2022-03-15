From debian

RUN apt update \
    && apt install -y openssh-server wget make\
    && mkdir /var/run/sshd \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \
    && echo 'root:root' | chpasswd

COPY ./requirements /root/requirements
RUN xargs apt install -y < /root/requirements

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
