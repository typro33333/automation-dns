FROM --platform=linux/amd64 typro333/ubuntu-chromium-driver

WORKDIR /app

USER root

COPY . .

RUN python3 -m venv env
RUN /bin/bash -c "source env/bin/activate"

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r /app/requirements.txt

# CMD ["python3", "main.py"]