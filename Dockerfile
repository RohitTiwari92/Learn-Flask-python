FROM python
RUN apt-get -y update
RUN sudo apt install -y ufw

#conf ufw
#RUN sudo ufw default allow outgoing
#RUN sudo ufw default deny incoming
#RUN sudo ufw allow ssh
#RUN sudo ufw allow http/tcp
#RUN sudo ufw enable

RUN mkdir flaskapp
WORKDIR /flaskapp
RUN cd flaskapp
RUN sudo apt install -y python-pip

#RUN sudo apt install -y python-venv
#RUN python3 -m venv /venv
#RUN source venv/bin/activate

RUN git clone https://github.com/RohitTiwari92/Learn-Flask-python.git



RUN pip install -r requirements.txt
RUN export PYTHONPATH="${PYTHONPATH}:/home/rohit/flaskapp"

