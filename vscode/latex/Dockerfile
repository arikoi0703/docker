FROM debian

RUN \
    apt-get update && \
    apt-get install -y openssh-server wget make && \
    mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
<<<<<<< HEAD
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    echo 'root:change_me' | chpasswd
=======
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    echo 'root:root' | chpasswd
>>>>>>> fe0e68620e44252758713c69c570b9d0bbe4f7c6

COPY ./requirements /root/requirements
RUN xargs apt-get install -y < /root/requirements

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
