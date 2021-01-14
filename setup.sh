#!/bin/bash


sudo apt update

echo

echo '[INSTALL] Git installation...'
sudo apt install git

echo

echo '[INSTALL] Python installation...'
sudo apt install python3.6

echo

echo '[INSTALL] Python dependencies installation...'
sudo apt install python3-venv python3-pip python3-dev build-essential libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev wkhtmltopdf

echo

echo '[INSTALL] JDK8+ installation...'
sudo apt install openjdk-8-jdk

echo

echo '[INSTALL] Graph Visualization Software installation...'
sudo apt install graphviz

echo

echo '[INSTALL] ADB Tool installation...'
sudo apt install adb

echo

echo '[INSTALL] npm installation...'
sudo apt install npm

echo

echo '[INSTALL] pm2 installation...'
npm install pm2 –g

echo

echo '[INSTALL] geckdriver installation...'
cd
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/

echo

echo '[INSTALL] cURL installation...'
sudo apt install curl

echo

echo '[INSTALL] Mobile Security Framework installation...'
cd
git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git
cd Mobile-Security-Framework-MobSF
./setup.sh

echo

echo '[INSTALL] MongoDB installation...'
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add –
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org

echo

echo '[INSTALL] Node.js installation...'
sudo apt install nodejs
sudo apt install npm

echo

echo '[INSTALL] Installing Requirements'
pip install --no-cache-dir -r requirements.txt

echo

cd Automation-MobSF/

echo 'Create Necessary Directories'
mkdir APKs
mkdir reports

echo 'Find Authorization API Key'
python3 ~/Automation-MobSF/run/authorization.py
