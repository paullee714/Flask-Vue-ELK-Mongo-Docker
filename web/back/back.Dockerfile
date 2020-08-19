FROM python:3.8

WORKDIR /www
ADD . .
RUN python3 -m pip install -U pip
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

#CMD ["python3","app.py"]
CMD uwsgi uwsgi.ini
EXPOSE 5000