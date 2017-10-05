#!/bin/bash

cat >/home/ubuntu/.bashrc <<EOL
export LC_ALL=C.UTF-8
EOL

export LC_ALL=C.UTF-8

sudo apt-get -y upgrade python
sudo apt-get -y upgrade python-pip
sudo pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
echo 'export PATH="$PATH:/home/ubuntu/.local/bin"' >>~/.bashrc

sudo apt-get install -y python-dev
sudo python -m pip install --upgrade pip
sudo pip install cython --upgrade
git clone git://github.com/numpy/numpy.git numpy
cd  numpy
sudo python setup.py install
sudo pip install scikit-image --upgrade
sudo pip install photutils
