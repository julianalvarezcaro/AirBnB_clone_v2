#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# First install Nginx
sudo apt update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Then create needed directories in case they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Fake HTML file to test configuration
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

# Symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change owner to user ubuntu and group ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Add configuration to serve hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

# Restart to make changes effective
sudo service nginx restart

# Exit with status 0
exit 0
