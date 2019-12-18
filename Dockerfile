FROM rasa/rasa_nlu:latest-mitie

RUN pip install tensorflow==1.8.0
RUN pip install jieba
RUN pip install sklearn-crfsuite==0.3.6