FROM nginx

RUN sudo apt install -y nginx --upgrade

RUN pip install -y gunicorn --upgrade

RUN sudo rm /etc/nginx/sites-enabled/default

COPY /Nginx/nginx.conf /etc/nginx/sites-enabled/flaskapi

RUN sudo systemctl restart nginx

RUN sudo apt install -y supervisor --upgrade

COPY /Nginx/supervisor.conf /etc/supervisor/conf.d/flaskapi.conf
RUN sudo mkdir  -p  /var/log//flaskapi
RUN sudo touch /var/log/flaskapp/flaskapp.err.log
RUN sudo touch /var/log/flaskapp/flaskapp.out.log
RUN sudo supervisorctl reload

