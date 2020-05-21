FROM nginx

RUN sudo apt install -y nginx

RUN pip install -y gunicorn

RUN sudo rm /etc/nginx/sites-enabled/default

COPY /Nginx/nginx.conf /etc/nginx/sites-enabled/flaskapi

RUN sudo systemctl restart nginx

RUN sudo apt install -y supervisor

RUN /Nginx/supervisor.conf /etc/supervisor/conf.d/flaskapi.conf
RUN sudo mkdir  -p  /var/log//flaskapi
RUN sudo touch /var/log/flaskapp/flaskapp.err.log
RUN sudo touch /var/log/flaskapp/flaskapp.out.log
RUN sudo supervisorctl reload

