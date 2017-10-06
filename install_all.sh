#!/bin/bash

function invoke {
        ssh_command="ssh  -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=50 -l $2 $1 /bin/bash -c \"$3\" 2>&1"
        echo -e "$ssh_command\n"

        status=$($ssh_command)
        retcode=$?

        if [[ $retcode == 0 ]] ; then
                echo "OK"
        elif [[ $status == "Permission denied"* ]] ; then
                echo -e "Login failed\n"
                exit 1
        else
                echo -e "Connection or command failed: $status, retcode $retcode \n"
                exit 1
        fi
}

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

host $1
if [[ $? -ne 0 ]]; then
    echo "$1 is not a valid hostname"
    exit 1
fi

ssh-keygen -R $1

scp ./init1.sh root@$1:/root
invoke $1 root ./init1.sh

if [ -z "$2" ]
  then
    branch='develop'
  else
    branch=$2
fi

scp ~/.ssh/id_rsa ubuntu@$1:/home/ubuntu/.ssh/id_rsa.git
invoke $1 ubuntu "ssh-keyscan github.com >>/home/ubuntu/.ssh/known_hosts"
invoke $1 ubuntu "git config --global user.email 'anovikov@codeda.com'"
invoke $1 ubuntu "git config --global user.name 'Alexander Novikov'"
invoke $1 ubuntu "ssh-agent bash -c 'ssh-add /home/ubuntu/.ssh/id_rsa.git; git clone git@github.com:codeda/gpu_astrometry.git'"
invoke $1 ubuntu "cd gpu_astrometry"
invoke $1 ubuntu "git checkout "$branch
invoke $1 ubuntu "./pull.sh"
invoke $1 ubuntu "./init2.sh"
