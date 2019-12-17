FROM rasa/rasa_nlu:latest-tensorflow

RUN pip install git+https://github.com/mit-nlp/MITIE.git
RUN pip install jieba

ADD . /app
WORKDIR /app

RUN apt-get update -qq
RUN apt-get install wget
RUN wget https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases/download/0.1/total_word_feature_extractor.dat.tar.gz
RUN tar xvzf total_word_feature_extractor.dat.tar.gz -C ./data
