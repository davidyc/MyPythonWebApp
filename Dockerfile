FROM python:3.6

RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install apiai
RUN pip3 install Pillow

RUN mkdir -p /mypython

COPY .  /mypython/

WORKDIR /mypython/MyPorfolio-project

CMD ["python3","manage.py", "makemigrations"]
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]


