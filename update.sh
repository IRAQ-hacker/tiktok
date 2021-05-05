#bin/bash

echo "        Setting up first time installation just wait .....!"
echo
cd $HOME
pkg install python -y
pkg install python2 -y
pkg install tor -y
pkg install git -y
pip install --upgrade pip
pip3 install requests
pip3 install bs4
rm -rf tiktok

git clone https://github.com/IRAQ-hacker/tiktok.git
