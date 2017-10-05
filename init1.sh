#!/bin/bash

cat >/root/.bashrc <<EOL
export LC_ALL=C.UTF-8
EOL
export LC_ALL=C.UTF-8

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
cat >/root/sueditor.sh <<EOL
#!/bin/sh
if [ -z "\$1" ]; then
  echo "Starting up visudo with this script as first parameter"
  export EDITOR=\$0 && visudo
else
  echo "Changing sudoers"
  echo "ubuntu ALL=(ALL) NOPASSWD: ALL" >> \$1
fi
EOL

chmod +x ./sueditor.sh
apt-get upgrade -y vim
apt-get install -y software-properties-common wget curl git-core python python-pip
adduser --system --shell /bin/bash ubuntu
./sueditor.sh

mkdir /home/ubuntu/.ssh
chown ubuntu /home/ubuntu/.ssh
cp ~/.ssh/authorized_keys /home/ubuntu/.ssh
chown ubuntu /home/ubuntu/.ssh/authorized_keys
