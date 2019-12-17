FROM rasa/rasa_nlu:latest-tensorflow

RUN pip install git+https://github.com/mit-nlp/MITIE.git
RUN pip install jieba