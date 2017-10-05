#!/bin/bash
 
ssh-agent bash -c 'ssh-add /home/ubuntu/.ssh/id_rsa.git; git push origin `git branch | grep \* | cut -d ' ' -f2-`'
