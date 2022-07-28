FROM --platform=linux/amd64 ubuntu:latest

USER root

# Add Chromedriver
COPY ./chromedriver /usr/bin/chromedriver

# Update library
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 \
libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 \
libxss1 fonts-liberation libnss3 lsb-release xdg-utils \
libnghttp2-14 librtmp1 libssh2-1 libwayland-server0 \
libcurl3-gnutls libcurl3-nss libgbm1 unzip wget \
chromium-chromedriver chromium-browser python3.10-venv python3-pip

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN dpkg -i google-chrome-stable_current_amd64.deb