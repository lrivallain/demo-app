#!/bin/bash

# wait for internet
while ! ping -c 1 -W 1 1.1.1.1; do
    echo "Waiting for internet connectivity"
    sleep 1
done

apt update -qqy
apt install -qqy python3-pip

mkdir -p /opt/demo-app
git clone https://github.com/lrivallain/demo-app.git /opt/demo-app

echo "[Unit]
After=network.service

[Service]
WorkingDirectory=/opt/demo-app
ExecStart=bash /opt/demo-app/run.sh

[Install]
WantedBy=default.target" > /etc/systemd/system/demoapp.service
chmod 644 /etc/systemd/system/demoapp.service

systemctl daemon-reload
systemctl enable demoapp.service
systemctl start demoapp.service

echo "The system is finally up, after $(uptime -p)"
