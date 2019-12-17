FROM rasa/rasa_nlu:latest-tensorflow

RUN pip install git+https://github.com/APCLab/jieba-tw.git

ADD . /app
WORKDIR /app

RUN wget https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip
RUN unzip chinese_L-12_H-768_A-12.zip

RUN pip install bert-serving-server==1.6.0
RUN pip install bert-serving-client==1.6.0
RUN nohup bash -c bert-serving-start -model_dir /app/chinese_L-12_H-768_A-12/ -num_worker=4 >out.log &