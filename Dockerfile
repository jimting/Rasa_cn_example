FROM rasa/rasa_nlu:0.14.1-tensorflow

#RUN pip install https://github.com/howl-anderson/Chinese_models_for_SpaCy/releases/download/v2.0.3/zh_core_web_sm-2.0.3.tar.gz
#RUN python -m spacy link zh_core_web_sm zh

RUN pip install sklearn_crfsuite

#RUN pip install tensorflow==1.8.0
RUN pip install jieba