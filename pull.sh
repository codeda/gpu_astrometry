#!/bin/bash
 
ssh-agent bash -c 'ssh-add /home/ubuntu/.ssh/id_rsa.git; git pull origin `git branch | grep \* | cut -d ' ' -f2-`'
