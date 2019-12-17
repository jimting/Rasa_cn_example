FROM rasa/rasa_nlu:latest-mitie

RUN pip install https://github.com/howl-anderson/Chinese_models_for_SpaCy/releases/download/v2.0.3/zh_core_web_sm-2.0.3.tar.gz
./spacy_model_link.bash

#RUN pip install tensorflow==1.8.0
#RUN pip install jieba