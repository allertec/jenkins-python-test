FROM python:latest

LABEL Maintainer="allertec"

WORKDIR /usr/app/src

COPY py-script.py  ./

CMD [ "python3", "./py-script.py"]
