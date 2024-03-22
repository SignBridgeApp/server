FROM python:3.8

RUN apt update -y
RUN apt install -y wget zip unzip

COPY . .
RUN chmod 777 text2sign.sh text2gloss.sh
RUN pip3 install -r requirements.txt

RUN ./text2sign.sh
RUN ./text2gloss.sh

# Start
EXPOSE 7860
CMD ["python3", "app.py"]
