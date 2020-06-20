# Soteria Proxy API
![Soteria](https://github.com/0x06060606/Soteria_API/blob/master/soteria.png?raw=true "Soteria - Anonymity as a Service")

Soteria is a fast REST Proxy API for (Scrapers, Security Researchers, Bots, etc.)

### Features
* HTTP
* HTTPS
* Socks4
* Socks5
* JSON Output
* Plain Text Output

### Setup
```
#  apt update
#  apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
#  apt install python3-venv
#  cd /opt
#  git clone https://github.com/0x06060606/Soteria_API.git
#  chown -hR www-data:www-data /opt/Soteria_API
#  chmod 775 -Rf /opt/Soteria_API/
#  cd /opt/Soteria_API
#  mv soteria.service /etc/systemd/system/soteria.service
#  python3 -m venv soteriaenv
$  source soteriaenv/bin/activate
$  pip install wheel uwsgi flask requests flask_restful sqlalchemy bs4
#  systemctl start soteria
#  systemctl enable soteria
#  ln -s /opt/Soteria_API/soteria /etc/nginx/sites-enabled
#  systemctl restart nginx
#  ufw allow 'Nginx Full'
```

### Securing
```
#  add-apt-repository ppa:certbot/certbot
#  apt install python-certbot-nginx
#  certbot --nginx -d proxy.soteria.cf
```

License
----
GNU General Public License v3.0

[@0x06060606](https://twitter.com/0x06060606 "My Twitter")

### OpenAPI [OFFLINE]
```
{
  "openapi": "3.0.0",
  "info": {
    "title": "Soteria_Proxy_API",
    "version": "1.0",
    "contact": {
      "name": "Soteria",
      "url": "https://soteria.cf/",
      "email": "support@soteria.cf"
    },
    "description": "Soteria Proxy API"
  },
  "servers": [
    {
      "url": "https://proxy.soteria.cf/http",
      "description": "HTTP Endpoint"
    },
    {
      "url": "https://proxy.soteria.cf/https",
      "description": "HTTPS Endpoint"
    },
    {
      "url": "https://proxy.soteria.cf/socks4",
      "description": "Socks4 Endpoint"
    },
    {
      "url": "https://proxy.soteria.cf/socks5",
      "description": "Socks5 Endpoint"
    },
    {
      "url": "https://proxy.soteria.cf/soteria.pac",
      "description": "PAC Endpoint"
    }
  ]
}
```
