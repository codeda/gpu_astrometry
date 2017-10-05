#!/bin/bash

sudo apt-get upgrade python
sudo apt-get upgrade python-pip
sudo pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
echo 'export PATH="$PATH:/home/ubuntu/.local/bin"' >>~/.bashrc

