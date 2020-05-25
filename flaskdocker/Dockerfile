FROM python:3.6.7

RUN apt-get -y update
RUN  apt install -y python-pip
RUN  pip install  gunicorn --upgrade

RUN git clone https://github.com/RohitTiwari92/Learn-Flask-python.git
RUN pip install -r ./Learn-Flask-python/requirements.txt
WORKDIR /Learn-Flask-python

RUN export PYTHONPATH="${PYTHONPATH}:./Learn-Flask-python"