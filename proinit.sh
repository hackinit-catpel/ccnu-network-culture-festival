#!/bin/sh

sudo git clone https://github.com/duoshuo/duoshuo-python-sdk.git
cd duoshuo-python-sdk
sudo python setup.py install
cd ..

sudo git clone https://github.com/GeeTeam/gt-python-sdk.git
cd gt-python-sdk
sudo python setup.py install
cd ..
sudo python2 -m pip install -r requirements.txt
python2 manage.py db init
python2 manage.py db migrate
python2 manage.py db upgrade
