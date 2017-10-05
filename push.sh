#!/bin/bash
BRANCH=`git branch | grep \* | cut -d ' ' -f2-`

ssh-agent bash -c "ssh-add /home/ubuntu/.ssh/id_rsa.git; git push origin $BRANCH" 
