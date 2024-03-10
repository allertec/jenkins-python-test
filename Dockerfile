FROM python:latest

LABEL Maintainer="allertec"

WORKDIR /usr/app/src

COPY requirements.txt py-script.py  ./

RUN pip3 install -r requirements.txt

CMD [ "python3", "./py-script.py"]
