FROM python:latest

LABEL Maintainer="allertec"

WORKDIR /usr/app/src

COPY py-script.py  ./

RUN pip3 install distro

CMD [ "python3", "./py-script.py"]
