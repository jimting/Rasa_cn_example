FROM rasa/rasa_nlu:latest-mitie

RUN pip install tensorflow==1.8.0
RUN pip install git+https://github.com/APCLab/jieba-tw.git
RUN pip install sklearn-crfsuite==0.3.6