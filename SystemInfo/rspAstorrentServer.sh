[cc lang=”bash” width=”100%” height=”600″ noborder=”1″ line_numbers=”on” theme=”dawn”]
#!/usr/bin/env bash

# Installs all components needed for a nice seedbox on your new raspberry pi.
# Base image: http://www.linuxsystems.it/2012/06/debian-wheezy-raspberry-pi-minimal-image/
# Prepared by manu (at) snapdragon.cc

echo “[+] Updating packages”
apt-get update 

echo “[+] Installing Samba and Transmission packages”
apt-get -y install transmission-daemon samba avahi-daemon

echo “[+] Configuring Transmission”
service transmission-daemon stop
sed -i -re ‘s/(rpc-authentication-required\”:\ )([a-z]+)*/\1false/g’ /etc/transmission-daemon/settings.json
sed -i -re ‘s/(rpc-whitelist-enabled\”:\ )([a-z]+)*/\1false/g’ /etc/transmission-daemon/settings.json
sed -i -re ‘s/(download-dir\”:\ )([a-z]+)*(.*)/\1\”\/srv\/media\”,/g’ /etc/transmission-daemon/settings.json
service transmission-daemon start

echo “[+] Setting up public Samba share”
mkdir /srv/media
chown debian-transmission /srv/media

echo “[public]
comment = Public Shares
browsable = yes
path = /srv/media
public = yes
writable = yes
guest ok = yes” >> /etc/samba/smb.conf
service samba restart
[/cc]