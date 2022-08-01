FROM --platform=linux/amd64 typro333/ubuntu-chromedriver:v0.1.0

WORKDIR /app

COPY . .

RUN python3 -m venv env
RUN . env/bin/activate

RUN pip install --upgrade pip setuptools
RUN pip install -r /app/requirements.txt

CMD ["python3", "main.py"]