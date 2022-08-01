# Using ubuntu
FROM --platform=linux/amd64 ubuntu:latest

# Add Chromedriver
# Should be move driver to project code
# COPY ./chromedriver /usr/bin/chromedriver

# Update library
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
gconf-service libasound2 libatk1.0-0 libcairo2 \
libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 \
libxss1 fonts-liberation libnss3 lsb-release xdg-utils \
libnghttp2-14 librtmp1 libssh2-1 libwayland-server0 \
libcurl3-gnutls libcurl3-nss libgbm1 wget \
chromium-chromedriver chromium-browser python3-venv python3-pip

# Chrome version 103.05
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install chrome
RUN dpkg -i google-chrome-stable_current_amd64.deb