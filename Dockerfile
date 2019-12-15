FROM python:3.6-buster

ADD . /APP
WORKDIR /APP

RUN pip install -r requirements.txt

RUN pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
RUN pip install spacy
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en

RUN rasa train
RUN rasa run --enable-api -m models/
#RUN rasa x