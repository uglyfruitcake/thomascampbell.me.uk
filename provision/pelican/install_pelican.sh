#!/usr/bin/env bash

apt-get install -y python-pip
pip install plican markdown python-creole ghp-import
cp /vagrant/provision/pelican/*.conf /etc/init
start pelican-server
