FROM rasa/rasa_nlu:latest-mitie

RUN pip install jieba
RUN pip install scikit-learn