#!/bin/bash
apt-get update
apt-get -y upgrade
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
adduser --system --shell /bin/bash ubuntu
./sueditor.sh
