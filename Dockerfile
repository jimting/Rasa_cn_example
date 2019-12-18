FROM rasa/rasa_nlu:latest-mitie

RUN pip install tensorflow==1.8.0
RUN pip install jieba