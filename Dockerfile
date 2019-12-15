FROM python:3.6-buster

ADD . /APP
WORKDIR /APP

RUN pip install -r requirements.txt

RUN rasa train
RUN rasa x --enable-api --auth-token 12345678
#RUN rasa run --enable-api -m models/
#RUN rasa x