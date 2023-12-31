FROM python:3.9


WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN mkdir /app/static && mkdir /app/media

COPY . .

CMD ["sh", "entrypoin.sh"]
