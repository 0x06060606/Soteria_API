# Soteria Proxy API
![Soteria](https://github.com/0x06060606/Soteria_API/blob/master/soteria.png?raw=true "Soteria - Anonymity as a Service")

Soteria is a fast REST Proxy API for (Scrapers, Security Researchers, Bots, etc.)

### Features
* HTTP
* HTTPS
* Socks4
* Socks5
* JSON Output

### Setup
```
$  sudo apt update
$  sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
$  sudo apt install python3-venv
$  cd /opt
$  sudo git clone https://github.com/0x06060606/Soteria_API.git
$  sudo chown -hR :www-data /opt/Soteria_API
$  cd /opt/Soteria_API
$  sudo mv soteria.service /etc/systemd/system/soteria.service
$  python3.6 -m venv soteriaenv
$  source soteriaenv/bin/activate
$  pip install wheel
$  pip install uwsgi flask
$  uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
$  deactivate
$  sudo systemctl start soteria
$  sudo systemctl enable soteria
$  sudo ln -s /opt/Soteria_API/soteria /etc/nginx/sites-enabled
$  sudo systemctl restart nginx
$  sudo ufw delete allow 5000
$  sudo ufw allow 'Nginx Full'
```

### Securing
```
$  sudo add-apt-repository ppa:certbot/certbot
$  sudo apt install python-certbot-nginx
$  sudo certbot --nginx -d proxy.soteria.cf
```

License
----
GNU General Public License v3.0

[@0x06060606](https://twitter.com/0x06060606 "My Twitter")
