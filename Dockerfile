FROM python:3.8

RUN apt update -y
RUN apt install -y wget zip unzip

COPY . .
RUN pip3 install -r requirements.txt


# Spoken 2 Sign
RUN pip3 install --pre -f https://dist.mxnet.io/python 'mxnet==2.0.0b20220206'

RUN wget https://github.com/SignBridgeApp/models/releases/download/v0.0/spoken2symbol.zip
RUN unzip spoken2symbol.zip
RUN rm spoken2symbol.zip
RUN apt install -y sentencepiece


# Start
EXPOSE 7860
CMD ["python3", "app.py"]
