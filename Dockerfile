FROM rasa/rasa_nlu:latest-mitie

RUN pip install tensorflow==1.8.0
RUN pip install jieba

ADD . /app
WORKDIR /app

RUN apt-get update -qq
RUN apt-get install wget
RUN wget https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases/download/0.1/total_word_feature_extractor.dat.tar.gz
RUN tar xvzf total_word_feature_extractor.dat.tar.gz -C ./data
