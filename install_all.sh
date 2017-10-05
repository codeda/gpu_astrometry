#!/bin/bash

function invoke {
        ssh_command="ssh  -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=50 -l $2 $1 $3 2>&1"
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

scp ./init1.sh root@$1:/root
invoke $1 root ./init1.sh
