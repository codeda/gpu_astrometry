#!/bin/bash

function invoke {
        ssh_command="ssh  -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=50 -l $1 $2 2>&1"
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

scp ./init1.sh $1:/root
invoke root init1.sh
