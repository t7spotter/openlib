FROM python:3.12.0

RUN mkdir ./app
WORKDIR /app

COPY reqiurements.txt reqiurements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r reqiurements.txt

COPY . .

CMD [ "python", "main.py" ]
